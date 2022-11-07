from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _


# Create your models here.
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
    qntDiasColheita = models.IntegerField
    qntPlantada = models.IntegerField
    dtPlantio = models.DateTimeField(default=datetime.today)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    areacultivo = models.ForeignKey(AreaCultivo, on_delete=models.CASCADE, null=True)
    colhida = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.descricao


class Irrigacao_Programacao(models.TextChoices):
    NAO_REPETE = 'NAO_REPETE', _('Não se repete')
    TODOS_DIAS = 'TODOS_DIAS', _('Todos os dias')
    PERSONALIZAR = 'PERSONALIZAR', _('Personalizar...')


class Irrigacao(models.Model):
    horario = models.DateTimeField()
    duracao = models.TimeField()
    concluida = models.BooleanField(blank=False, null=False, default=False)
    plantacao = models.ForeignKey(Plantacao, on_delete=models.CASCADE)
    programacao = models.TextField(choices=Irrigacao_Programacao.choices, max_length=20, null=True, default=0)
