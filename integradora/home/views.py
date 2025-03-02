from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def acerca(request):
    return render(request, 'home/acerca.html')

def asesoramiento(request):
    return render(request, 'home/asesoramiento.html')

def contacto(request):
    return render(request, 'home/contacto.html')