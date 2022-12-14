from datetime import datetime

from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker

from .models import *


class FormAreas(forms.ModelForm):

    class Meta:
        model = AreaCultivo
        fields = '__all__'
        labels = {'nome':'Nome da Área'}


class FormPlantacoes(forms.ModelForm):

    class Meta:
        model = Plantacao
        fields = '__all__'
    
class FormIrrigacoes(forms.ModelForm):
    class Meta:
        model = Irrigacao
        fields = '__all__'

class FormTarefas(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
       

class formUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username','email','avatar',]
       