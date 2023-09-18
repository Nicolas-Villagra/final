from django.db import models

# Create your models here.
class Cargar(models.Model):
    nombre=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to="media/")
    descripcion=models.CharField(max_length=200)
    email=models.CharField(max_length=30)
    direccion=models.URLField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} - {self.email} "
