from datetime import datetime

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Users(AbstractUser):
    avatar = models.ImageField("Icone do perfil",upload_to='', null=True, blank=True, default='nulo')
class Categoria(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


class AreaCultivo(models.Model):
    nome = models.CharField(max_length=100)
    disponivel = models.BooleanField(blank=True, null=False, default=True)
    apta = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return self.nome


class Plantacao(models.Model):
    descricao = models.CharField(max_length=100)
    qntDiasColheita = models.IntegerField(null=True)
    qntPlantada = models.IntegerField(null=True)
    qntColhida = models.IntegerField(null=True)
    dtPlantio = models.DateTimeField(default=datetime.today)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    areacultivo = models.ForeignKey(AreaCultivo, on_delete=models.CASCADE, null=True)
    colhida = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.descricao


class Irrigacao_Programacao(models.TextChoices):
    NAO_REPETE = 'NAO_REPETE', _('Não se repete')
    TODOS_DIAS = 'TODOS_DIAS', _('Todos os dias')

class Tipos_Tarefa(models.TextChoices):
    PLANTACAO = 'PLANTACAO', _('Em uma plantação')
    AREA = 'AREA', _('Em uma área')
    LIVRE = 'LIVRE', _('Livre')

class Irrigacao(models.Model):
    dtUltIrrigacao = models.DateField(null=True, blank=True)
    dtProxIrrigacao = models.DateField(default=datetime.today, null=True, blank=True)
    horario = models.TimeField()
    duracao = models.TimeField()
    concluida = models.BooleanField(blank=False, null=False, default=False)
    plantacao = models.ForeignKey(Plantacao, on_delete=models.CASCADE)
    programacao = models.TextField(choices=Irrigacao_Programacao.choices, max_length=20, null=True, default=0)


class Tarefa(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.DateField(default=datetime.today)
    tipoTarefa = models.TextField(choices=Tipos_Tarefa.choices, max_length=20, null=True, default=0)
    areacultivo = models.ForeignKey(AreaCultivo, on_delete=models.CASCADE, null=True, blank=True)
    plantacao = models.ForeignKey(Plantacao, on_delete=models.CASCADE, null=True, blank=True)
    concluida = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return self.descricao