from django.urls import path 
from main import views

urlpatterns = [
    path('', views.showWelcomePage),
    path("signin/", views.showSignin),
    path("signup/", views.showSignup),
    path("forgotpassword/", views.showForgotPass),
    path("forgotpass/", views.validateForgotPass),
    path("logout/", views.logoutProcess),
    path("uploadVideo/", views.uploadVideo),
    path("signupvalidate/", views.signUpValidate),
    path("upload/", views.signInValidate),
    path("process/", views.videoProcess ),
    path("reportSubmit/", views.reportSubmit),
]