from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar, FamiliarForm  
from django.views import View 

# Create your views here.

def index(request):
    return render(request, "ejemplo/saludar.html",{"nombre":"asdf","apellido":"lepori"})

def imc(request, peso, altura):
    calculo_imc =  float(peso)/float(altura)
    return render(request,"ejemplo/imc.html",{"peso":peso,"altura":altura, "calculo_imc":calculo_imc})

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View): # hereda de view

    form_class = Buscar #define un atributo de clase, donde buscar es el import que se importo
    template_name = 'ejemplo/buscar.html' # ruta del template
    initial = {"nombre":""} #campo nombre por defecto esta vacio

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form}) # variable form azul se encuentra en template buscar,  self.template "envia el template"

    def post(self, request):
        form = self.form_class(request.POST) # envia la consulta que viene del campo nombre
        if form.is_valid(): # valida que no tenga mas de 100 caracteres la consulta, si no es valido retorna error por django
            nombre = form.cleaned_data.get("nombre")# cleaned data - limpia datos y genera un diccionario. Get es para diccionario.
            #campo nombre es la misma variable que form, tiene que respetarse 
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() # i May o min / contains trae el stream completo o incompleto
            form = self.form_class(initial=self.initial) # resetea el formulario para posteriores consultas
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})



