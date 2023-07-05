from django.contrib import admin

from django.urls import path,include

from . import views

from .views import report, pdf , pdfss
from django.contrib.auth import views as auth_views




urlpatterns = [
        path('',views.home, name="home"),
        path('signup',views.signup,name="signup"),
        path('signin',views.signin,name="signin"),
        path('signout',views.signout,name="signout"),
        path('activate/<uidb64>/<token>',views.activate,name="activate"),
        path('list/',views.lyra_list, name="lyra_list"),
        path('list/<int:pk>/',views.lyra_detail, name="lyra_detail"),
        path('report/',report,name="report"),
        path('pdf/', pdf, name="pdf"),
        path('pdfs/', pdfss, name="pdfss"),
        
        #reset
       
        path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
        path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

   
]

















