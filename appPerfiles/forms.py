from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import *


class CargarForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    imagen=forms.ImageField(label="imagen")
    descripcion=forms.CharField(max_length=200)
    email=forms.CharField(max_length=30)
    direccion=forms.URLField(max_length=50)