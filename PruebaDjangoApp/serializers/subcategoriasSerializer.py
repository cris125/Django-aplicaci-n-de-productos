from rest_framework import serializers
from PruebaDjangoApp.models.Subcategorias import Subcategorias

class SubcategoriasSerializer(serializers.ModelSerializer):
   class Meta:
       model = Subcategorias
       fields = ['id', 'nombre','descripcion'] 
    

