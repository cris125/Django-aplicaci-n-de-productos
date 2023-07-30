from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from PruebaDjangoApp.models.Categorias import Categorias
from PruebaDjangoApp.serializers.CategoriasSerializer import CategoriasSerializer
from django.shortcuts import redirect, render


class CategoriasView(views.APIView):
    queryset = Categorias.objects.all()
    Categorias_class = CategoriasSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = CategoriasSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return redirect('/EditCategoria/')
    
    def get(self, request, *args, **kwargs):
        '''
        List all the branch for given requested user
        '''
        categorias = Categorias.objects.all()
        serializer = CategoriasSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
