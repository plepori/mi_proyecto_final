from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView  # <----- NUEVO IMPORT
from ejemplo.models import Familiar


class FamiliarList(ListView):
  model = Familiar

class FamiliarCrear(CreateView):
    model = Familiar
    success_url = "/panel-familia"
    fields = ["nombre", "direccion", "numero_pasaporte"]

class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"

class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]