from django.db import models

# Create your models here.
class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    construido_por = models.CharField(max_length=30)
    titulo_principal = models.CharField(max_length=30,default='')
    subtitulo_principal = models.CharField(max_length=30,default='')






