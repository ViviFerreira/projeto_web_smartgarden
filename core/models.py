from statistics import mode

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=45)


class AreaCultivo(models.Model):
    nome = models.CharField(max_length=100)


class Plantação(models.Model):
    descrição = models.CharField(max_length=100)
    qntDiasColheita = models.IntegerField
    qntPlantada = models.IntegerField
    dPlantio = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    areacultivo = models.ForeignKey(AreaCultivo, on_delete=models.CASCADE)


class Irrigação(models.Model):
    horario = models.DateTimeField(auto_now_add=True)
    duração = models.TimeField(auto_now_add=True)
    flConcluida = models.BooleanField
    plantacao = models.ForeignKey(Plantação, on_delete=models.CASCADE)
