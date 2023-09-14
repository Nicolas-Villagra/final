from django.http import *
from django.shortcuts import render
from appLogin.views import obtenerAvatar


#Contiene Avatar.!
def inicio(request):

    avatar=obtenerAvatar(request)

    return render(request,"templates/inicio.html",{"Avatar":obtenerAvatar(request)})


#Contiene Avatar.!
def acercademi(request):
    avatar=obtenerAvatar(request)
    return render (request, "templates/acercademi.html",{"Avatar":obtenerAvatar(request)})