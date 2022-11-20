from django.contrib import auth, messages
from django.contrib.messages import constants
from django.core.paginator import Paginator
from django.db.models.aggregates import Count
from django.db.models.signals import post_save
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from datetime import timedelta
from django.contrib.auth.decorators import login_required

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
            user = Users.objects.create_user(
                username=username, email=email, password=senha
            )
            user.save()
            return render(request, "login_usuario.html")
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

@login_required(login_url='/')
def inicio(request):
    
    areas = AreaCultivo.objects.all()
    dataset = Plantacao.objects.all()

    qntDisponivel = AreaCultivo.objects.filter(disponivel=True).count()
    qntOcupado = AreaCultivo.objects.filter(disponivel=False).count()
   
    labels = []
    qtdsPlantadas = []
    qtdsColhidas = []
    statusAreas = [qntDisponivel,qntOcupado]


    for plantacao in dataset:
        labels.append(plantacao.descricao)
        qtdsPlantadas.append(plantacao.qntPlantada)
        qtdsColhidas.append(plantacao.qntColhida)

    contexto = {
        'labels':labels,
         'qtdsPlantadas':qtdsPlantadas, 
         'qtdsColhidas':qtdsColhidas, 
         'statusAreas': statusAreas
    }

    return render(request, 'inicio.html',contexto)


@login_required(login_url='/')
def areas(request):
    areas = AreaCultivo.objects.all()
    qntDisponivel = AreaCultivo.objects.filter(disponivel=True).count()
    qntOcupado = AreaCultivo.objects.filter(disponivel=False).count()
    qntApta = AreaCultivo.objects.filter(apta=True).count()
    qntInapta = AreaCultivo.objects.filter(apta=False).count()

    paginator = Paginator(areas, 6)
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


@login_required(login_url='/')
def cadastrar_areas(request):
    form = FormAreas(request.POST or None)
    area = AreaCultivo.objects.filter(nome=request.POST.get("nome"))
    
    if(area):
        messages.error(request, 'Essa área já existe, informe um nome diferente')
        
    elif form.is_valid():
        form.save()
        messages.success(request, 'Área de cultivo cadastrada com sucesso!')
        
    
    contexto = {'form': form}
    return render(request, 'cadastrar_areas.html', contexto)


@login_required(login_url='/')
def update_areas(request, id):
    area = AreaCultivo.objects.get(id=id)
    form = FormAreas(instance=area)

    if request.method == 'POST':
        form = FormAreas(request.POST, instance=area)
        if form.is_valid():
            form.save()
            messages.success(request, 'Área de cultivo atualizada com sucesso!')
            return redirect('areas')
    return render(request, 'update_areas.html', {'formareas': form})


@login_required(login_url='/')
def delete_areas(request, id):
    area = get_object_or_404(AreaCultivo, pk=id)
    area.delete()
    return redirect("areas")


@login_required(login_url='/')
def plantacoes(request):
    plantacoes = Plantacao.objects.all()

    paginator = Paginator(plantacoes, 6)
    page = request.GET.get('page')
    plantacoes = paginator.get_page(page)

    contexto = {
        'plantacoes': plantacoes
    }   
    return render(request, 'plantações.html', contexto)

@login_required(login_url='/')
def update_plantacoes(request,id):
    plantacoes = Plantacao.objects.get(id=id)

    form = FormPlantacoes(instance=plantacoes)
    
    if request.method == 'POST':
        form = FormPlantacoes(request.POST, instance=plantacoes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Plantação atualizada com sucesso!')
            return redirect('plantacoes')
    return render(request, 'update_plantacoes.html', {'formplant': form})

@login_required(login_url='/')
def update_colhida(request,id):
    plantacoes = Plantacao.objects.get(id=id)
    form = FormPlantacoes(instance=plantacoes)
    
    if request.method == 'POST':
        qntColhida = request.POST.get("qntColhida")
        
        if Plantacao.objects.filter(id=id).update(qntColhida=qntColhida, colhida=True):
            return redirect('plantacoes')

    return render(request, 'update_colhida.html', {'formplant': form})

@login_required(login_url='/')
def update_irrigada(request,id):   
    irrigacao = Irrigacao.objects.get(id=id)
    if irrigacao.programacao != 'TODOS_DIAS': 
        ultima_irrigacao = irrigacao.dtProxIrrigacao
        Irrigacao.objects.filter(id=id).update(concluida=True, dtUltIrrigacao=ultima_irrigacao)
    if irrigacao.programacao == 'TODOS_DIAS':
        ultima_irrigacao = irrigacao.dtProxIrrigacao
        proxima_irrigacao = ultima_irrigacao + timedelta(1)
        Irrigacao.objects.filter(id=id).update(dtUltIrrigacao=ultima_irrigacao, dtProxIrrigacao=proxima_irrigacao)

    return redirect('irrigacoes')

@login_required(login_url='/')
def update_tarefa_concluida(request,id):    
    Tarefa.objects.filter(id=id).update(concluida=True)

    return redirect('tarefas')

@login_required(login_url='/')
def cadastrar_plantacoes(request):
    form = FormPlantacoes(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Sua plantação foi cadastrada com sucesso!')

    contexto = {'form': form}
    
    return render(request, 'cadastrar_plantacoes.html', contexto)

@login_required(login_url='/')
def delete_plantacoes(request, id):
    plantacoes = get_object_or_404(Plantacao, pk=id)
    plantacoes.delete()
    return redirect("plantacoes")

@login_required(login_url='/')
def irrigacoes(request):
    irrigacoes = Irrigacao.objects.all()

    paginator = Paginator(irrigacoes, 6)
    page = request.GET.get('page')
    irrigacoes = paginator.get_page(page)

    contexto = {
        'irrigacoes': irrigacoes
    }   
    return render(request, 'irrigacoes.html', contexto)

@login_required(login_url='/')
def update_irrigacoes(request,id):
    irrigacoes = Irrigacao.objects.get(id=id)

    form = FormIrrigacoes(instance=irrigacoes)
    if request.method == 'POST':
        form = FormIrrigacoes(request.POST, instance=irrigacoes)
        if form.is_valid():
            form.save()
            return redirect('irrigacoes')
    return render(request, 'update_irrigacoes.html', {'formirr': form})

@login_required(login_url='/')
def delete_irrigacoes(request, id):
    irrigacoes = get_object_or_404(Irrigacao, pk=id)
    irrigacoes.delete()
    return redirect("irrigacoes")


@login_required(login_url='/')
def cadastrar_tarefas(request):
    form = FormTarefas(request.POST or None)
    tipo_tarefa = request.POST.get("tipoTarefa")
    area_cultivo = request.POST.get("areacultivo")
    plantacao = request.POST.get("plantacao")

    if tipo_tarefa == 'AREA' and not area_cultivo:
        messages.error(request, 'Por favor, informe uma área de cultivo!')
    elif tipo_tarefa == 'PLANTACAO' and not plantacao:
        messages.error(request, 'Por favor, informe uma plantação!')
    elif form.is_valid():
        form.save()
        messages.success(request, 'Sua tarefa cadastrada com sucesso!')
    contexto = {'form': form}
    return render(request, 'cadastrar_tarefas.html', contexto)

@login_required(login_url='/')
def tarefas(request):
    tarefas = Tarefa.objects.all()

    paginator = Paginator(tarefas, 6)
    page = request.GET.get('page')
    tarefas = paginator.get_page(page)
    contexto = {
        'tarefas': tarefas
    }   
    return render(request, 'tarefas.html', contexto)

@login_required(login_url='/')
def cadastrar_irrigacoes(request):
    form = FormIrrigacoes(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'A irrigação foi cadastrada com sucesso!')
    else:
        print(form)

    contexto = {'form': form}

    return render(request, 'cadastrar_irrigacoes.html', contexto)

@login_required(login_url='/')
def update_tarefas(request,id):
    tarefas = Tarefa.objects.get(id=id)
    form = FormTarefas(instance=tarefas)

    if request.method == 'POST':
        form = FormTarefas(request.POST, instance=tarefas)

        tipo_tarefa = request.POST.get("tipoTarefa")
        area_cultivo = request.POST.get("areacultivo")
        plantacao = request.POST.get("plantacao")

        if tipo_tarefa == 'AREA' and not area_cultivo:
            messages.error(request, 'Por favor, informe uma área de cultivo!')
        elif tipo_tarefa == 'PLANTACAO' and not plantacao:
            messages.error(request, 'Por favor, informe uma plantação!')
        elif form.is_valid():
            form.save()
            return redirect('tarefas')

    return render(request, 'update_tarefas.html', {'formtar': form})

@login_required(login_url='/')
def delete_tarefas(request, id):
    tarefas = get_object_or_404(Tarefa, pk=id)
    tarefas.delete()
    return redirect("tarefas")


@login_required(login_url='/')
def atualizar_area(sender, instance, created, **kwargs): 
    if created:
        AreaCultivo.objects.filter(nome=instance.areacultivo).update(disponivel=False)
      
post_save.connect(atualizar_area, sender=Plantacao)


@login_required(login_url='/')
def editar_perfil(request,id):
    user= Users.objects.get(id=id)
    form = formUser(instance=user)
    if request.method == 'POST':
        form = formUser(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('areas')
    return render(request, 'editar_perfil.html', {'formuser': form})

def sobre(request):
    return render(request,'sobre.html')

   
def handler404(request, exception):
    return render(request,'not_found.html')
