from django.contrib import auth, messages
from django.contrib.messages import constants
from django.core.paginator import Paginator
from django.db.models.aggregates import Count
from django.db.models.signals import post_save
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import *
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
        return render(request, "login_usuario.html")
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

    paginator = Paginator(areas, 3)
    page = request.GET.get('page')
    areas = paginator.get_page(page)

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
        return redirect('cadastrar_areas')
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

def update_plantacoes(request,id):
    plantacoes = Plantacao.objects.get(id=id)
    form = FormPlantacoes(instance=plantacoes)
    if request.method == 'POST':
        form = FormPlantacoes(request.POST, instance=plantacoes)
        if form.is_valid():
            form.save()
            return redirect('plantacoes')
    return render(request, 'update_plantacoes.html', {'formplant': form})

def cadastrar_plantacoes(request):
    form = FormPlantacoes(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Sua plantação foi cadastrada com sucesso!')

    contexto = {'form': form}

    return render(request, 'cadastrar_plantacoes.html', contexto)

def delete_plantacoes(request, id):
    plantacoes = get_object_or_404(Plantacao, pk=id)
    plantacoes.delete()
    return redirect("plantacoes")

def irrigacoes(request):
    irrigacoes = Irrigacao.objects.all()
    contexto = {
        'irrigacoes': irrigacoes
    }   
    return render(request, 'irrigacoes.html', contexto)


def cadastrar_tarefas(request):
    form = FormTarefas(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Sua tarefa cadastrada com sucesso!')
    contexto = {'form': form}
    return render(request, 'cadastrar_tarefas.html', contexto)

def tarefas(request):
    tarefas = Tarefa.objects.all()
    contexto = {
        'tarefas': tarefas
    }   
    return render(request, 'tarefas.html', contexto)

def cadastrar_irrigacoes(request):
    form = FormIrrigacoes(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'A irrigação foi cadastrada com sucesso!')
    else:
        print(form)

    contexto = {'form': form}

    return render(request, 'cadastrar_irrigacoes.html', contexto)


def atualizar_area(sender, instance, created, **kwargs): 
    if created:
        AreaCultivo.objects.filter(nome=instance.areacultivo).update(disponivel=False)
      
post_save.connect(atualizar_area, sender=Plantacao)


