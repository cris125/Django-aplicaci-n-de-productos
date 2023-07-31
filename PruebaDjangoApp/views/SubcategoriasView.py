from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from PruebaDjangoApp.models.Subcategorias import Subcategorias
from PruebaDjangoApp.serializers.subcategoriasSerializer import SubcategoriasSerializer
from django.shortcuts import redirect, render


class SubcategoriasView(views.APIView):
    queryset = Subcategorias.objects.all()
    Categorias_class = SubcategoriasSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = SubcategoriasSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return redirect('/EditSubcategoria/')
    
    
    def get(self, request, *args, **kwargs):
        '''
        List all the branch for given requested user
        '''
        subcategorias = Subcategorias.objects.all()
        serializer = SubcategoriasSerializer(subcategorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    