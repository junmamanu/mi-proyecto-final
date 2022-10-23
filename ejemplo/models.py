from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Usuarios(models.Model):
    usuario = models.CharField(max_length = 30)
    contraseña = models.CharField(max_length = 30)
    nombre_apellido = models.CharField(max_length = 50)
    


