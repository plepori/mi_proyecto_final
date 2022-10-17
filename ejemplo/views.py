from django.shortcuts import render
from ejemplo.models import Familiar

# Create your views here.

def index(request):
    return render(request, "ejemplo/saludar.html",{"nombre":"asdf","apellido":"lepori"})

def imc(request, peso, altura):
    calculo_imc =  float(peso)/float(altura)
    return render(request,"ejemplo/imc.html",{"peso":peso,"altura":altura, "calculo_imc":calculo_imc})

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})
