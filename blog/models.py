from django.db import models

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    costruido_por =models.CharField(max_length=30)
    titulo_principal =models.CharField(max_length=30, default = "")
    subtitutulo_principal = models.CharField(max_length=30, default ="")