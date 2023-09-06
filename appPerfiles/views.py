from django.shortcuts import render
from .forms import UsuarioForm
from .models import *
from appLogin.views import obtenerAvatar

# Create your views here.
def Usuario(request):
    if request.method=="POST":
        form=UsuarioForm(request.POST) 
        if  form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            imangen=info["imagen"]
            descripcion=info["turno"]
            mail=info["mail"]
            usuario= UsuarioForm (nombre=nombre, imagen=request.FILES["imagen"], descripcion=descripcion, mail=mail)
            usuario.save()
            mensaje="Creado"
            
        else:
            mensaje="Datos Invalidos"

        form_usuario=UsuarioForm()
        return render(request,"templates/inicio.html", {"mensaje":mensaje, "formulario":form,"Avatar":obtenerAvatar(request) })
    else:
       usuario=Usuario.objects.all()
    form_usuario=UsuarioForm()
    return render(request,"template/usuario.html", {"formulario":form,"Usuario":usuario})

def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    usuario = Usuario.objects.all()
    formulario_Usuario=UsuarioForm()
    mensaje="Usuario Eliminado"
    return render(request,"templates/eliminarUsuario.html", {"mensaje": mensaje,"formulario":formulario_Usuario, "Usuario":usuario})

def editarUsuario(request, id):
    usuario=Usuario.objects.get(id=id)
    if request.method=="POST":
        form=UsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.nombre=["nombre"]
            usuario.imagen=info["imagen"]
            usuario.descripcion=info["descripcion"]
            usuario.mail=info["mail"]
            usuario.save()
            mensaje="usuario Editado"
            usuario=Usuario.objects.all()
            formulario_cliente=UsuarioForm()
            return render (request, "gimnasioApp/editarsuario.html",{"mensaje":mensaje,"formulario": formulario_cliente, "Usuario":usuario})
    else:

        usuario=Usuario.objects.get(id=id)
        usuario=UsuarioForm(initial= {"nombre":usuario.nombre,"imagen":request.FILES["imagen"],"descripcion":usuario.descripcion,"mail":usuario.mail})
        return render(request, "gimnasioApp/editarUsuario.html", {"formulario":usuario, "clientes":usuario})
    

def busquedaUsuario(request):
    return render (request, "template/busquedaUsuario.html")

def buscar(request):
    nombre=request.GET["nombre"]
    if nombre!="":
       Usuario=Usuario.objects.filter(nombre__icontains=nombre)
       return render(request,"template/resultado.html",{"Usuario":Usuario})
    else:
        return render (request,"templates/busquedaUsuario.html")