from django.urls import path
from .views import *


urlpatterns = [

path("cargar/", cargar, name="cargar"),

path("elimininarCargar/", eliminarCargar, name="eliminarCargar"),

path("editarcargar/", editarcargar, name="editarcargar"),

path("buscar/", buscar, name="buscar"),

path("listar_cargar/", listar_cargar, name="listar_cargar",)
]
