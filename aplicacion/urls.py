from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home" ),
    path('servicios/', servicios, name="servicios" ),
    path('vehiculos/', vehiculos, name="vehiculos" ),
    path('productos/', productos, name="productos" ),
    path('agregarServicio/', agregarServicio, name="agregarServicio" ),
    path('agregarVehiculo/', agregarVehiculo, name="agregarVehiculo" ),
    path('agregarProducto/', agregarProducto, name="agregarProducto" ),
    path('busquedaServicio/', busquedaServicio, name="busquedaServicio" ),
    path('buscarServicio/', buscarServicio, name="buscarServicio" ),
    path('busquedaVehiculo/', busquedaVehiculo, name="busquedaVehiculo" ),
    path('buscarVehiculo/', buscarVehiculo, name="buscarVehiculo" ),
    path('busquedaProducto/', busquedaProducto, name="busquedaProducto" ),
    path('buscarProducto/', buscarProducto, name="buscarProducto" ),
]