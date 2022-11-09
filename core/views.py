from django.contrib import auth, messages
from django.contrib.messages import constants
from django.db.models.aggregates import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models.signals import post_save

from .forms import FormAreas, FormPlantacoes
from .models import *

# Create your views here.


def cadastrar_usuarios(request):
    if request.method == "GET":
        return render(request, "cadastrar_usuarios.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        try:
            user = User.objects.create_user(
                username=username, email=email, password=senha
            )
            user.save()
            return render(request, "home.html")
        except:
            return render(request, "cadastrar_usuarios.html")


def login(request):
    if request.method == "GET":
        return render(request, "home.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)

        if not user:
            messages.add_message(
                request, constants.ERROR, "Username ou senha inválidos"
            )
            return redirect("/")
        else:
            auth.login(request, user)
            return redirect("inicio/")


def logout(request):
    auth.logout(request)
    return redirect("/")


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

    return render(request, 'areas.html', contexto)


def cadastrar_areas(request):
    form = FormAreas(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Área de cultivo cadastrada com sucesso!')
    contexto = {'form': form}
    return render(request, 'cadastrar_areas.html', contexto)


def update_areas(request, id):
    area = AreaCultivo.objects.get(id=id)
    form = FormAreas(instance=area)

    if request.method == 'POST':
        form = FormAreas(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect('areas')
    return render(request, 'update_areas.html', {'formareas': form})


def delete_areas(request, id):
    area = get_object_or_404(AreaCultivo, pk=id)
    area.delete()
    return redirect("areas")


def plantacoes(request):
    plantacoes = Plantacao.objects.all()
    contexto = {
        'plantacoes': plantacoes
    }   
    return render(request, 'plantações.html', contexto)


def irrigacoes(request):
    return render(request, 'irrigações.html')


def cadastrar_plantacoes(request):
    form = FormPlantacoes(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Sua plantação foi cadastrada com sucesso!')

    contexto = {'form': form}

    return render(request, 'cadastrar_plantacoes.html', contexto)

def atualizar_area(sender, instance, created, **kwargs): 
    if created:
        AreaCultivo.objects.filter(nome=instance.areacultivo).update(disponivel=False)
      
post_save.connect(atualizar_area, sender=Plantacao)

def editarAreas(request):
    return render(request, 'editar_areas.html')
