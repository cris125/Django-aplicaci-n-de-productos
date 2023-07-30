from django.db import models
from .Subcategorias import Subcategorias

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Productos', max_length=50)
    descripción = models.CharField('descripción', max_length=50)
    precio= models.FloatField()
    foto= models.ImageField(upload_to='static/images/')
    cantidad = models.FloatField()
    subcategoria =  models.ForeignKey(Subcategorias, on_delete=models.CASCADE)