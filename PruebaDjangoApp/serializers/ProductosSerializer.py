from rest_framework import serializers
from PruebaDjangoApp.models.Productos import Productos

class ProductosSerializer(serializers.ModelSerializer):
   class Meta:
       foto = serializers.ImageField(max_length=None, use_url=True)
       model = Productos
       fields = ['id', 'nombre','descripción','precio','foto','cantidad','subcategoria'] 
    


