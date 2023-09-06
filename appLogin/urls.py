from django.urls import path
from .views import *
from django.contrib.auth.views import *
from django.contrib.auth import *
from django.contrib.auth.forms import *





urlpatterns = [

   #login
   path("login/", login_request, name="login"),
   
   #logout 
   path("logout/", LogoutView.as_view(), name="logout"),

   #editar perfil
   path("editarPerfil/", editarPerfil, name="editarPerfil"),


   path("obtenerAvatar", obtenerAvatar, name="obtenerAvatar"),

   path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),

   ]
