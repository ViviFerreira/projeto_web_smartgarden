from unicodedata import name

from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cad/', views.cad, name='cadastro'),
    path("logout/", views.logout, name="logout"),
    path('inicio/', views.inicio, name='inicio'),
    path('areas/', views.areas, name='areas'),
    path('areas/cadastrar_areas/', views.cadastrar_areas, name='cadastrar_areas')
]
