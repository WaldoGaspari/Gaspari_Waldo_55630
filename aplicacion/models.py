from django.db import models

class Servicio(models.Model):

    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)

class Vehiculo(models.Model):

    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    tipo = models.CharField(max_length=20)

class Producto(models.Model):

    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    uso = models.CharField(max_length=60)

