from unicodedata import name

from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastrar_usuarios/', views.cadastrar_usuarios,
         name='cadastrar_usuarios'),
    path('logout/', views.logout, name="logout"),
    path('inicio/', views.inicio, name='inicio'),
    path('areas/', views.areas, name='areas'),
    path('cadastrar_areas/', views.cadastrar_areas, name='cadastrar_areas'),
    path('update_areas/<int:id>', views.update_areas, name='update_areas'),
    path('delete_areas/<int:id>', views.delete_areas, name='delete_areas'),
    path('plantacoes/', views.plantacoes, name='plantacoes'),
    path('cadastrar_plantacoes/', views.cadastrar_plantacoes,
         name='cadastrar_plantacoes'),
]
