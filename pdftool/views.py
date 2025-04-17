from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator

from certify import settings
from .tokens import generate_token
from .models import Lyra, Student
from .pdf import html2pdf
from .constants import data_dict_1, data_dict_2, data_dict_3, data_dict_4, data_dict_5


# Home Page
def home(request):
    return render(request, "pdftool/index.html")


# User Signup
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists! Please try something else.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('home')

        if len(username) > 12:
            messages.error(request, "Username must be under 12 characters.")
            return redirect('home')

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.is_active = False
        myuser.save()

        # Welcome Email
        subject = "Welcome to PDFTOOL - LYRA Login!!"
        message = f"Hi {myuser.first_name}!\n\nWelcome to LYRA!\nThanks for signing up. We have sent you a confirmation email. Please confirm your email address to activate your account.\n\nThank You!\nTeam LYRA"
        send_mail(subject, message, settings.EMAIL_HOST_USER, [myuser.email], fail_silently=True)

        # Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your email @ PDFTOOL - LYRA Login!!"
        message2 = render_to_string('pdftool/email_configuration.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser),
        })
        email = EmailMessage(email_subject, message2, settings.EMAIL_HOST_USER, [myuser.email])
        email.fail_silently = True
        email.send()

        messages.success(request, "Account created successfully. Please check your email to confirm.")
        return redirect("signin")

    return render(request, "pdftool/signup.html")


# Email Activation
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')


# User Signin
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Send password reset email if user does not exist
            uid = urlsafe_base64_encode(force_bytes(username))
            token = default_token_generator.make_token(user)
            domain = request.META['HTTP_HOST']
            reset_link = f"http://{domain}{reverse('password_reset_confirm', args=[uid, token])}"
            subject = "Password Reset Request"
            message = f"Hi,\nWe received a request to reset your password. Click the link below:\n{reset_link}\n\nIf you didn’t request it, ignore this email."
            send_mail(subject, message, 'pdftool.lyra@gmail.com', [username])
            messages.success(request, "Password reset link has been sent to your email.")
            return redirect('home')

        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('report')
        else:
            messages.error(request, "Incorrect username or password.")
            return redirect('signin')

    return render(request, "pdftool/signin.html")


# User Signout
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')


# Report Page
def report(request):
    return render(request, 'pdftool/report.html')


# Generate PDF Based on User
def pdf(request):
    user = request.user
    username = user.username
    data_dict = {}

    if username == 'Kavya':
        data_dict = data_dict_1
    elif username == 'Amala':
        data_dict = data_dict_2
    elif username == 'Sakthi':
        data_dict = data_dict_3
    elif username == 'Aishwarya':
        data_dict = data_dict_4
    elif username == 'Joshika':
        data_dict = data_dict_5

    pdf1 = html2pdf("pdftool/pdf.html", data_dict)
    return HttpResponse(pdf1.getvalue(), content_type="application/pdf")


# List of All Students from Lyra
def lyra_list(request):
    lyras = Lyra.objects.all()
    return render(request, 'pdftool/lyra_list.html', {'lyras': lyras})


# Detail View for a Specific Lyra Student
def lyra_detail(request, pk):
    lyra = get_object_or_404(Lyra, pk=pk)
    return render(request, 'pdftool/lyra_detail.html', {'lyra': lyra})


# All Lyra Data for PDF View
def pdfss(request):
    datas = Lyra.objects.all()
    return render(request, 'pdftool/pdf2.html', {'datas': datas})


# First Student Info Display
def student_info(request):
    student = Lyra.objects.first()
    return render(request, 'pdftool/index.html', {'student': student})


# All Students in Student Table
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
