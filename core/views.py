from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count
from .forms import FormAreas
from .models import *

 #Create your views here.
def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')

def areas(request):
    areas = AreaCultivo.objects.all()
    qntDisponivel = AreaCultivo.objects.filter(disponivel=True).count()
    qntOcupado = AreaCultivo.objects.filter(disponivel=False).count()
    qntApta = AreaCultivo.objects.filter(apta=True).count()
    qntInapta = AreaCultivo.objects.filter(apta=False).count()

    contexto = {
        'areas': areas, 
        'qntDisponivel': qntDisponivel,
        'qntOcupado': qntOcupado,
        'qntApta': qntApta,
        'qntInapta': qntInapta,
    }

    return render(request, 'areas.html', contexto )

def cadastrar_areas(request):
    form = FormAreas(request.POST or None)
    if form.is_valid():
        form.save()
    contexto = {'form':form}

    return render(request, 'cadastrar_areas.html', contexto)

def teste(request):
    qntDisponivel = AreaCultivo.objects.filter(disponivel=True).count()

    return HttpResponse(qntDisponivel)