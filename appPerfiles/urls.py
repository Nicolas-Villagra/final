from django.urls import path
from .views import *


urlpatterns = [

path("cargar/", cargar, name="cargar"),

path("elimininarCargar/", eliminarCargar, name="eliminarCargar"),

path("editarcargar/", editarcargar, name="editarcargar"),

path("busquedacargar/", busquedacargar, name="busquedacargar"),

path("buscar/", buscar, name="buscar"),


]
