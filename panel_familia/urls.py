from django.urls import path
from panel_familia.views import  FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar

urlpatterns = [
    path('', FamiliarList.as_view(), name="familiar-list"), # NUEVA RUTA PARA LISTAR FAMILIAR   
    path('crear', FamiliarCrear.as_view(), name="familiar-crear"), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('<int:pk>/borrar', FamiliarBorrar.as_view(), name="familiar-borrar"), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('<int:pk>/actualizar', FamiliarActualizar.as_view(), name="familiar-actualizar"),
]