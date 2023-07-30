from django.db import models

from .Categorias import Categorias

class Subcategorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('subcategoria', max_length=50)
    descripcion = models.CharField(max_length=100, default='descripcion')
    
    



