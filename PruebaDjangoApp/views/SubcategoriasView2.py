from audioop import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from PruebaDjangoApp.models.Subcategorias import Subcategorias
from django.contrib import messages
from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from PruebaDjangoApp.serializers.subcategoriasSerializer import SubcategoriasSerializer
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add(request):
    queryset = Subcategorias.objects.all()
    SupCategorias_class = SubcategoriasSerializer
    serializer = SubcategoriasSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
                       
    return redirect('/EditSubcategoria/')

@login_required
def delete( request, pk):
      subcategorias =Subcategorias.objects.get(pk=pk)
      subcategorias.delete()
      messages.success(request, '¡Categorias eliminado!')
      return redirect("/EditSubcategoria/")

@login_required
def edicionP(request, pk):
    subcategoria = Subcategorias.objects.get(pk=pk)
    return render(request, "EditarCategoria.html", {"subcategoria": subcategoria})

@login_required
def editarP(request,pk):
    nombre = request.POST['nombre']
    descripcion=request.POST['descripcion']

    subcategorias = Subcategorias.objects.get(pk=pk)
    subcategorias.nombre = nombre
    subcategorias.descripcion=descripcion

    subcategorias.save()
    messages.success(request, '¡subcategorias actualizado!')

    return redirect('/EditCategoria/')

@login_required
def categoria(request):
  subcategoria = Subcategorias.objects.all().values()
  context = {
    'subcategoria': subcategoria
  }
  
  template =loader.get_template('AddSupcategoria.html')
  return HttpResponse(template.render(context, request))
