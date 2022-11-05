from django.contrib import auth, messages
from django.contrib.messages import constants
from django.db.models.aggregates import Count
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import FormAreas
from .models import *

# Create your views here.


def cad(request):
    if request.method == "GET":
        return render(request, "cad.html")
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
            return render(request, "cad.html")


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
