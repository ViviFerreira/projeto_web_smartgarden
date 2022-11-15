from django.urls import path

from . import views

urlpatterns = [
    path('sobre/',views.sobre, name='sobre'),
    path('', views.login, name='login'),
    path('cadastrar_usuarios/', views.cadastrar_usuarios,name='cadastrar_usuarios'),
    path('logout/', views.logout, name="logout"),
    path('inicio/', views.inicio, name='inicio'),
    path('areas/', views.areas, name='areas'),
    path('cadastrar_areas/', views.cadastrar_areas, name='cadastrar_areas'),
    path('update_areas/<int:id>', views.update_areas, name='update_areas'),
    path('delete_areas/<int:id>', views.delete_areas, name='delete_areas'),
    path('plantacoes/', views.plantacoes, name='plantacoes'),
    path('cadastrar_plantacoes/', views.cadastrar_plantacoes, name='cadastrar_plantacoes'),
    path('update_plantacoes/<int:id>', views.update_plantacoes, name='update_plantacoes'),
    path('update_colhida/<int:id>', views.update_colhida, name='update_colhida'),
    path('delete_plantacoes/<int:id>', views.delete_plantacoes, name='delete_plantacoes'),
    path('irrigacoes/' ,views.irrigacoes, name='irrigacoes'),
    path('cadastrar_irrigacoes/' ,views.cadastrar_irrigacoes, name='cadastrar_irrigacoes'),
    path('cadastrar_tarefas/' ,views.cadastrar_tarefas, name='cadastrar_tarefas'),
    path('tarefas/' ,views.tarefas, name='tarefas'),
    #path('perfil/' ,views.perfil, name='perfil'),
    path('editar_perfil/<int:id>' ,views.editar_perfil, name='editar_perfil'),
]
