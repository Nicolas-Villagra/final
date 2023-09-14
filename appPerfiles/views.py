from django.shortcuts import render
from .forms import *
from .models import *
from appLogin.views import obtenerAvatar

# Create your views here.
def cargar(request):
    if request.method=="POST":
        form=CargarForm(request.POST) 
        if  form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            imagen=info["imagen"]
            descripcion=info["descripcion"]
            email=info["email"]
            cargar= CargarForm (nombre=nombre, imagen=request.FILES["imagen"], descripcion=descripcion, email=email)
            cargar.save()
            mensaje="Cargado..."
            
        else:
           mensaje="Datos Invalidos"

        formulario_cargar=CargarForm()
        return render(request,"templates/cargar.html", {"mensaje":mensaje, "formulario":formulario_cargar,"Avatar":obtenerAvatar(request) })
    else:
        formulario_cargar=CargarForm()
    cargar=Cargar.objects.all()
    return render(request,"templates/cargar.html", {"formulario":formulario_cargar,"Cargar":cargar })

def eliminarCargar(request, id):
    cargar =cargar.objects.get(id=id)
    cargar.delete()
    cargar = cargar.objects.all()
    formulario_cargar=CargarForm()
    mensaje="Eliminado"
    return render(request,"templates/cargar.html", {"mensaje": mensaje,"formulario":formulario_cargar, "cargar":cargar})

def editarcargar(request, id):
    Cargar=cargar.objects.get(id=id)
    if request.method=="POST":
        form=CargarForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            Cargar.nombre=["nombre"]
            Cargar.imagen=info["imagen"]
            Cargar.descripcion=info["descripcion"]
            Cargar.email=info["email"]
            Cargar.save()
            mensaje="Editado"
            Cargar=cargar.objects.all()
            formulario_cargar=CargarForm()
            return render (request, "templates/cargar.html",{"mensaje":mensaje,"formulario": formulario_cargar, "Cargar":cargar})
    else:

        Cargar=cargar.objects.get(id=id)
        Cargar=CargarForm(initial= {"nombre":cargar.nombre,"imagen":request.FILES["imagen"],"descripcion":cargar.descripcion,"email":cargar.email})
        return render(request, "templates/cargar.html", {"formulario":formulario_cargar, "Cargar":cargar})
    

def busquedacargar(request):
    return render (request, "template/busquedaUsuario.html")

def buscar(request):
    nombre=request.GET["nombre"]
    if nombre!="":
       cargar=cargar.objects.filter(nombre__icontains=nombre)
       return render(request,"template/resultado.html",{"cargar":cargar})
    else:
        return render (request,"templates/busquedaUsuario.html")
    

def listar_Usuario(request):
    cargar=cargar.objects.all()
    return render (request, "templates/resultado.html",{"cargar":cargar})