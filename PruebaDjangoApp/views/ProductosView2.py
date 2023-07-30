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
      messages.success(request, '¡Productos eliminado!')
      return redirect("/EditProductos/")

@login_required
def edicionP(request, pk):
    producto = Productos.objects.get(pk=pk)
    return render(request, "EditarProducto.html", {"producto": producto})

@login_required
def editarP(request,pk):
    nombre = request.POST['nombre']
    descripción=request.POST['descripción']
    precio=request.POST['precio']
    foto=request.POST['foto']
    cantidad=request.POST['cantidad']
    subcategoria=request.POST['subcategoria']

    producto = Productos.objects.get(pk=pk)
    producto.nombre = nombre
    producto.descripción=descripción
    producto.precio=precio
    producto.foto=foto
    producto.cantidad =cantidad 
    producto.subcategoria=subcategoria
    producto.save()
    

    return redirect('/EditProductos/')

@login_required
def categoria(request):
  productos = Productos.objects.all().values()
  context = {
    'productos': productos
  }
  template =loader.get_template('AddProducto.html')
  return HttpResponse(template.render(context, request))
