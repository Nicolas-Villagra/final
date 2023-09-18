from django.shortcuts import render
from .forms import *
from .models import *
from appLogin.views import obtenerAvatar

# Create your views here.
def cargar(request):
    if request.method=="POST":
        form=CargarForm(request.POST, request.FILES) 
        if  form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            imagen=info["imagen"]
            descripcion=info["descripcion"]
            email=info["email"]
            direccion=info["direccion"]
            cargar= Cargar(nombre=nombre, imagen=imagen, descripcion=descripcion, email=email, direccion=direccion)
            cargar.save()
            mensaje="Cargado..."
            
        else:
           mensaje="Datos Invalidos"

        formulario_cargar=CargarForm()
        return render(request,"templates/cargar.html", {"mensaje":mensaje,"formulario":formulario_cargar,"Avatar":obtenerAvatar(request) })
    else:
        formulario_cargar=CargarForm()
    cargar=Cargar.objects.all()
    return render(request,"templates/cargar.html", {"formulario":formulario_cargar,"Cargar":cargar, "Avatar":obtenerAvatar(request)})

def eliminarCargar(request, id):
    cargar =cargar.objects.get(id=id)
    cargar.delete()
    cargar = Cargar.objects.all()
    formulario_cargar=CargarForm()
    mensaje="Eliminado"
    return render(request,"templates/cargar.html", {"mensaje": mensaje,"formulario":formulario_cargar, "Cargar":cargar})

def editarcargar(request, id):
    cargar=Cargar.objects.get(id=id)
    if request.method=="POST":
        form=CargarForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            cargar.nombre=["nombre"]
            cargar.imagen=info["imagen"]
            cargar.descripcion=info["descripcion"]
            cargar.email=info["email"]
            cargar.direccion=info["direccion"]
            cargar.save()
            mensaje="Editado"
            cargar=Cargar.objects.all()
            formulario_cargar=CargarForm()
            return render (request, "templates/cargar.html",{"mensaje":mensaje,"formulario": formulario_cargar, "Cargar":cargar})
    else:

        cargar=Cargar.objects.get(id=id)
        cargar=CargarForm(initial= {"nombre":cargar.nombre,"imagen":request.FILES["imagen"],"descripcion":cargar.descripcion,"email":cargar.email, "direccion":cargar.direccion})
        return render(request, "templates/editarcargar.html", {"formulario":formulario_cargar, "Cargar":cargar})

def buscar(request):
    nombre=request.GET
    if nombre!="":
       cargar=Cargar.objects.all()
       return render(request,"templates/listar_cargar.html",{"Cargar":cargar})
    else:
        mensaje="no se encontraron resultados"
        return render (request,"templates/inicio.html",{"mensaje":mensaje})

def listar_cargar(request):
    cargar=Cargar.objects.all()
    contexto={"Cargar":cargar}
    return render (request, "templates/resultados.html",contexto)