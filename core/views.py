from django.shortcuts import render

 #Create your views here.
def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')

def verArea(request):
    return render(request, 'verArea.html')