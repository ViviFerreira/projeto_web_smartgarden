from django import forms
from datetime import datetime
from tempus_dominus.widgets import DatePicker
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
        labels = {
            'descricao': 'Descrição',
            'areacultivo':'Área de Cultivo',
            'dtPlantio': 'Data do Plantio'
        }
        widgets = {
            'dtPlantio':  DatePicker(),
        }
        
        