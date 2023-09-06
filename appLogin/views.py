from django.shortcuts import *
from .models import *
from django.http import *
from .forms import *
from .views import *
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render (request,"templates/inicio.html",{"mensaje": f"usuario {usu} logeado correctamente"})
            else:
                return render (request,"templates/login.html",{"mensaje":"Datos Incorrectos"})
        else:
            return render (request, "templates/login.html",{"formulario": form, "mensaje": "Datos Incorrectos"})
    else:
        form=AuthenticationForm()
        return render (request, "templates/login.html", {"formulario":form})

#contiene Avatar!
def editarPerfil(request):
        avatar=obtenerAvatar(request)
        usuario=request.user
        if request.method=="POST":
            form=UserEditForm(request.POST)
            if form.is_valid():
                info=form.cleaned_data
                usuario.email=info["email"]
                usuario.password1=info["password1"]
                usuario.password2=info["password2"]
                usuario.first_name=info["first_name"]
                usuario.last_name=info["last_name"]
                usuario.save()
                return render (request,"templates/inicio.html",{"mensaje":f"Usuario {usuario.first_name} Editado Correctamente","Avatar":obtenerAvatar(request)})
            else:
                return render (request,"templates/editarPerfil.html",{"formulario":form,"nombreusuario":usuario.username, "mensaje":"Datos Invalidos", "Avatar":obtenerAvatar(request)})
        
        else:
            form=UserEditForm(instance=usuario)
            return render (request, "templates/editarPerfil.html",{"formulario": form, "nombreusuario":usuario.username,"Avatar":obtenerAvatar(request)})

def obtenerAvatar(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "media/avatars/avatarpordefecto.png"     

def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])

            avatarviejo=Avatar.objects.filter(user=request.user)
            if len (avatarviejo)>0:
                avatarviejo[0].delete()
            avatar.save()
            return render (request, "templates/inicio.html", {"mensaje":"Avatar cargado correctamente", "Avatar":obtenerAvatar(request)})
        else:
            return render (request, "templates/agregarAvatar.html",{"formulario":form, "usuario":request.user, "Avatar":obtenerAvatar(request)})
    else:
        form=AvatarForm()
        return render (request, "templates/agregarAvatar.html",{"formulario":form, "usuario":request.user,"Avatar":obtenerAvatar(request)})