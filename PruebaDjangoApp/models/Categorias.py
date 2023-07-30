from django.db import models

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Categorias', max_length=50)
    


