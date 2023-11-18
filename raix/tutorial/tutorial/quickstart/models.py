from django.db import models

# Create your models here.

class Alumno(models.Model):
    nomUsuario = models.CharField(max_length=40, default='no especificado')
    nombre = models.CharField(max_length=30, default='no especificado')
    apellidoP = models.CharField(max_length=30, default='no especificado')
    apellidoM = models.CharField(max_length=30, default='no especificado')
    rut = models.TextField( default='no especificado')
    contraseña = models.CharField(max_length=20, default='no especificado')
    correo = models.EmailField(default='no especificado')

    def __str__(self):
        return self.nombre
    
class Clases(models.Model):
    nombre = models.CharField(max_length=30)
    sigla = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Asistencia(models.Model):
    nombreAlum = models.CharField(max_length=30)
    rutAlum = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre