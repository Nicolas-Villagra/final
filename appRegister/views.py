from django.shortcuts import render
from .models import *
from django.http import *
from django.contrib.auth.forms import *
from .forms import *



def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render (request, "templates/inicio.html", {"mensaje":f"Usuario {nombre_usuario} creado correctamente"})
        else:
            return render (request, "templates/register.html",{"formulario":form,"mensaje":"Datos Incorrectos"})
    else:
        form=RegistroUsuarioForm()
        return render (request, "templates/register.html",{"formulario":form})
    
