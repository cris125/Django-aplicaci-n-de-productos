from rest_framework import serializers
from PruebaDjangoApp.models.Productos import Productos

class ProductosSerializer(serializers.ModelSerializer):
   class Meta:
       model = Productos
       fields = ['id', 'nombre','descripción','precio','foto','cantidad','subcategoria'] 
    


