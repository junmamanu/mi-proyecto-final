from django.db import models

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    costruido_por =models.CharField(max_length=30)
    titulo_principal =models.CharField(max_length=30, default = "")
    subtitutulo_principal = models.CharField(max_length=30, default ="")

class Usuarios(models.Model):
    usuario = models.CharField(max_length = 30)
    contraseña = models.CharField(max_length = 30)
    nombre_apellido = models.CharField(max_length = 50)
    email = models.CharField(max_length= 30)
    pais = models.CharField(max_length = 30)
    
    def __str__(self):
        return f"{self.usuario} ,{self.nombre_apellido},{self.email},{self.pais}, {self.id}"
