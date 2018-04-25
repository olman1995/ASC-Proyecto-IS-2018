from django.db import models


class usuario(models.Model):
    nombre = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)
    tipo = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    
class paciente(models.Model):
    edad = models.IntegerField()
    estimacion_edad = models.IntegerField()
    url_imagen = models.CharField(max_length=200)
    nombre = models.CharField(max_length=20)
    apellido_1 = models.CharField(max_length=20)
    apellido_2 = models.CharField(max_length=20)
    cedula = models.IntegerField()
    hospital = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre
    
