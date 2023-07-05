
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from lyra1 import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token

from django.shortcuts import render, redirect

from .models import Lyra

from django.http import FileResponse



from django.shortcuts import render,HttpResponse
from .pdf import html2pdf





# Create your views here.
def home(request):
    return render(request, "pdftool/index.html")




def signup(request):

    if request.method == "POST":
        #studentname = request.POST.get('studentname')
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try something new")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')

        if len(username)>12:
            messages.error(request, "Username must be under 12 characters")
        
        if password1 != password2:
            messages.error(request, "Incorrect password!")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.lastname = lastname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your account have been successfully created. we have sent you a confirmation e-mail,please check your inbox and confirm your email inorder to activate your account")
       
        #Welcome Email

        subject = "Welcome to PDFTOOL - LYRA Login!!"
        message = "Hi" + myuser.first_name + "!!! \n" +"Welcome to LYRA! \n Thank You!! for signing in our website. \n We have sent you a configuration email, please confirm yor E-mail address inorder to activate your account. \n\n Thank You! Team lyra "
        from_email=settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        #Email address confirmation Email
        
        current_site = get_current_site(request)
        email_subject= "Confirm your email @ PDFTOOL - LYRA Login!!"
        message2 = render_to_string('pdftool/email_configuration.html',{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token' : generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        return redirect("signin")

    return render(request, "pdftool/signup.html")






from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator


from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import User



def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        # Check if the user exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # If user does not exist, send a password reset email
            token_generator = default_token_generator
            uid = urlsafe_base64_encode(force_bytes(username))
            token = token_generator.make_token(username)
            protocol = 'https' if request.is_secure() else 'http'
            domain = request.META['HTTP_HOST']
            reset_link = f"{protocol}://{domain}{reverse('password_reset_confirm', args=[uid, token])}"
            subject = "Password Reset Request"
            message = f"Someone asked for a password reset for email {username}. Follow the link below:\n\n{reset_link}\n\n"
            from_email = 'pdftool.lyra@gmail.com'
            recipient_list = [username]
            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, "An email has been sent to you with further instructions.")
            return redirect('home')

        # If the user exists, authenticate and log them in
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('report')
        else:
            messages.error(request, "Incorrect Username or Password!")
            return redirect('signin')

    return render(request, "pdftool/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser= User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')




# views.py
def lyra_list(request):
    lyras = Lyra.objects.all()
    return render(request, 'pdftool/lyra_list.html', {'lyras': lyras})

def lyra_detail(request, pk):
    lyra = get_object_or_404(Lyra, pk=pk)
    return render(request, 'lyra_detail.html', {'lyra': lyra})




def report(request):
    return render(request, 'pdftool/report.html',)

# Create your views here.


from .constants import data_dict_1, data_dict_2, data_dict_3

def pdf(request):
    user = request.user
    
    if user.username == 'Kavya':
        data_dict = data_dict_1
        
    if user.username == 'Amala':
        data_dict = data_dict_2

    if user.username == 'Sakthi':
        data_dict = data_dict_3

    if user.username == 'Aishwarya':
        data_dict = data_dict_4

    if user.username == 'Joshika':
        data_dict = data_dict_5
    
    pdf1 = html2pdf("pdftool/pdf.html", data_dict)
    return HttpResponse(pdf1.getvalue(), content_type="application/pdf")





def pdfss(request):
    datas= Lyra.objects.all()
    return render(request, 'pdftool/pdf2.html',{'datas':datas})
    

from django.shortcuts import render
from .models import Lyra

def student_info(request):
    student = Lyra.objects.first()  # get the first student in the database
    context = {'student': student}
    return render(request, 'pdftool/index.html', context)


from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'student_list.html', context)
