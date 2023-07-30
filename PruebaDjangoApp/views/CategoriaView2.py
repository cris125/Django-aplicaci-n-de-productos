from audioop import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from PruebaDjangoApp.models.Categorias import Categorias
from PruebaDjangoApp.serializers.CategoriasSerializer import CategoriasSerializer
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add(request):
    queryset = Categorias.objects.all()
    Categorias_class = CategoriasSerializer
    serializer = CategoriasSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
                       
    return redirect('/EditCategoria/')

@login_required   
def delete( request, pk):
      categorias = Categorias.objects.get(pk=pk)
      categorias.delete()
      messages.success(request, '¡Categorias eliminado!')
      return redirect("/EditCategoria/")

@login_required
def edicionP(request, pk):
    categoria = Categorias.objects.get(pk=pk)
    return render(request, "EditarCategoria.html", {"categoria": categoria})

@login_required
def editarP(request,pk):
    nombre = request.POST['nombre']

    producto = Categorias.objects.get(pk=pk)
    producto.nombre = nombre
    producto.save()
    messages.success(request, '¡Categorias actualizado!')

    return redirect('/EditCategoria/')

@login_required
def categoria(request):
  categoria = Categorias.objects.all().values()
  context = {
    'categoria': categoria
  }
  template =loader.get_template('AddCategoria.html')
  return HttpResponse(template.render(context, request))
