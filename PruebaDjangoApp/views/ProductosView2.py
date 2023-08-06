from audioop import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from PruebaDjangoApp.models.Productos import Productos
from django.contrib import messages
from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from PruebaDjangoApp.serializers.ProductosSerializer import ProductosSerializer
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from PruebaDjangoApp.models import Subcategorias


@login_required
def add(request):
    queryset =Productos.objects.all()
    SupCategorias_class = ProductosSerializer
    serializer =ProductosSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
                       
    return redirect('/EditProductos/')

@login_required    
def delete( request, pk):
  productos =Productos.objects.get(pk=pk)
  productos.delete()
  return redirect("/EditProductos/")

@login_required
def edicionP(request, pk):
    producto = Productos.objects.get(pk=pk)
    return render(request, "EditarProducto.html", {"producto": producto})

@login_required
def editarP(request,pk):
    
    nombre = request.POST['nombre']
    descripcion = request.POST['descripción']
    precio = request.POST['precio']
    cantidad = request.POST['cantidad']
    foto = request.FILES["foto"]
    subcategoria_id=request.POST["subcategoria"]
    subcategoria = Subcategorias.objects.get(pk=subcategoria_id)
  
    
    producto = Productos.objects.get(pk=pk)
    
    producto.nombre = nombre
    producto.descripción=descripcion
    producto.precio=precio
    producto.foto=foto
    producto.cantidad =cantidad 

    producto.subcategoria = subcategoria
   
    producto.save()
    
    return redirect('/EditProductos/')
    

    
    
@login_required
def categoria(request):
  productos = Productos.objects.all().values()
  subcategoria=Subcategorias.objects.all().values()
  subcategoria=len(subcategoria)
  context = {
    'productos': productos,
    'subcategoria':subcategoria
  }
  template =loader.get_template('AddProducto.html')
  return HttpResponse(template.render(context, request))
