from django.contrib import admin
from django.urls import path 
from users import views as users_views #view for registration is already present
from django.contrib.auth import view as auth_view #login ke liye view already in-built hota hai

urlpatterns = [
    path("register/",users_views.register, name="register"),
    path("login/",users_views.login, name="login")
     
]