from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django

from .forms1 import UserChangeForm, UserCreationForm
from .models import *
from .models import Users


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
admin.site.register(AreaCultivo, Listar_Areas)
admin.site.register(Plantacao, Listar_Plantacoes )
admin.site.register(Irrigacao, Listar_Irrigacoes)

@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Campos Novos', {'fields': ('avatar',)}),
    )
