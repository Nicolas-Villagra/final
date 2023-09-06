from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import *


class UsuarioForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    imagen=forms.ImageField(label="imagen")
    descripcion=forms.CharField(max_length=200)

    email=forms.CharField(max_length=30)
    contraseña=forms.CharField(max_length=50)
