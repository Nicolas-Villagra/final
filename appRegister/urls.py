from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView




urlpatterns = [
   #registro
   path("register", register, name="register"),

   ]

