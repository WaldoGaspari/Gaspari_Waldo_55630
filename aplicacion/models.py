from django.db import models

class Servicio(models.Model):

    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return f"Servicio: {self.nombre}"

class Vehiculo(models.Model):

    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return f"Vehículo: {self.marca}, Modelo: {self.modelo}"

class Producto(models.Model):

    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    uso = models.CharField(max_length=60)

    def __str__(self):
        return f"Producto: {self.nombre}, Marca: {self.marca}"

