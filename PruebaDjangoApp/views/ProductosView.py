from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from PruebaDjangoApp.models.Productos import Productos
from PruebaDjangoApp.serializers.ProductosSerializer import ProductosSerializer
from django.shortcuts import redirect, render


class ProductosView(views.APIView):
    queryset = Productos.objects.all()
    Productos_class = ProductosSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = ProductosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return redirect('/EditProductos/')
    
    def get(self, request, *args, **kwargs):
        '''
        List all the branch for given requested user
        '''
        productos = Productos.objects.all()
        serializer = ProductosSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def editarP(self, request, *args, **kwargs):
        pk=kwargs
        serializer = ProductosSerializer( data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        productos =Productos.objects.get(pk=pk)
        productos.delete()
        return redirect('/EditSubcategoria/')    
        

   