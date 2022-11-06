from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('inicio/', views.inicio, name='inicio'),
    path('areas/', views.areas, name='areas'),
    path('areas/cadastrar_areas/', views.cadastrar_areas, name='cadastrar_areas'),
    path('plantações/', views.plantacoes, name='plantacoes'),
]
