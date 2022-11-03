from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker
from datetime import datetime
from .models import *

class FormAreas(forms.ModelForm):

    class Meta:
        model = AreaCultivo
        fields = '__all__'
        labels = {'nome':'Nome da Área'}
        