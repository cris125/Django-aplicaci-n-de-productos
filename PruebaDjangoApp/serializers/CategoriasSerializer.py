from rest_framework import serializers
from PruebaDjangoApp.models.Categorias import Categorias

class CategoriasSerializer(serializers.ModelSerializer):
   class Meta:
       model = Categorias
       fields = ['id', 'nombre'] 
    


