from django.contrib import admin
from .models import *

class Listar_Plantacoes(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'categoria', 'areacultivo', 'dtPlantio', 'colhida')
    list_display_links = ('id', 'descricao')
    list_editable = ('colhida',)
    list_per_page = 10

class Listar_Areas(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    list_per_page = 10


class Listar_Irrigacoes(admin.ModelAdmin):
    list_display = ('id', 'plantacao', 'programacao', 'horario','duracao', 'concluida')
    list_display_links = ('id', 'plantacao')
    list_editable = ('concluida',)
    list_per_page = 10

# Register your models here.
admin.site.register(Categoria)
admin.site.register(AreaCultivo, Listar_Areas)
admin.site.register(Plantacao, Listar_Plantacoes )
admin.site.register(Irrigacao, Listar_Irrigacoes)
