from django.urls import path
from .views import *


urlpatterns = [

path("Usuario/", Usuario, name="Usuario"),

path("eliminarUsuario/<id>", eliminarUsuario, name="eliminarUsuario"),

path("editarUsuario/<id>", editarUsuario, name="editarUsuario"),

path("busquedaUsuario/", busquedaUsuario, name="busquedaUsuario"),

path("buscar/", buscar, name="buscar"),


]
