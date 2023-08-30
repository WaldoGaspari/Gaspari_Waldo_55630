from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    return render(request, "aplicacion/inicio.html")

def servicios(request):
    contexto = {'servicios': Servicio.objects.all()}
    return render(request, "aplicacion/servicios.html", contexto)

def vehiculos(request):
    contexto = {'vehiculos': Vehiculo.objects.all()}
    return render(request, "aplicacion/vehiculos.html", contexto)

def productos(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, "aplicacion/productos.html", contexto)

def agregarServicio(request):
    if request.method == "POST":
        formulario = FormularioServicio(request.POST)
        if formulario.is_valid():
            servicio_nombre = formulario.cleaned_data.get('nombre')
            servicio_tipo = formulario.cleaned_data.get('tipo')
            servicio_descripcion = formulario.cleaned_data.get('descripcion')
            servicio = Servicio(nombre=servicio_nombre, tipo=servicio_tipo, descripcion=servicio_descripcion)
            servicio.save()
            return render(request, "aplicacion/servicios.html", {'servicios': Servicio.objects.all()})
    else:
        formulario = FormularioServicio()
    
    return render(request, "aplicacion/agregarServicio.html", {"form": formulario })

def agregarVehiculo(request):
    if request.method == "POST":
        formulario = FormularioVehiculo(request.POST)
        if formulario.is_valid():
            vehiculo_marca = formulario.cleaned_data.get('marca')
            vehiculo_modelo = formulario.cleaned_data.get('modelo')
            vehiculo_tipo = formulario.cleaned_data.get('tipo')
            vehiculo = Vehiculo(marca=vehiculo_marca, modelo=vehiculo_modelo, tipo=vehiculo_tipo)
            vehiculo.save()
            return render(request, "aplicacion/vehiculos.html", {'vehiculos': Vehiculo.objects.all()})
    else:
        formulario = FormularioVehiculo()
    
    return render(request, "aplicacion/agregarVehiculo.html", {"form": formulario })

def agregarProducto(request):
    if request.method == "POST":
        formulario = FormularioProducto(request.POST)
        if formulario.is_valid():
            producto_nombre = formulario.cleaned_data.get('nombre')
            producto_marca = formulario.cleaned_data.get('marca')
            producto_uso = formulario.cleaned_data.get('uso')
            producto = Producto(nombre=producto_nombre, marca=producto_marca, uso=producto_uso)
            producto.save()
            return render(request, "aplicacion/productos.html", {'productos': Producto.objects.all()})
    else:
        formulario = FormularioProducto()
    
    return render(request, "aplicacion/agregarProducto.html", {"form": formulario })

def busquedaServicio(request):
    return render(request, "aplicacion/buscarServicio.html")

def buscarServicio(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        servicios = Servicio.objects.filter(nombre__icontains=patron)
        contexto = {"servicios": servicios, 'titulo': f'Patrón de búsqueda:"{patron}"'}
        return render(request, "aplicacion/servicios.html", contexto)
    return HttpResponse("No se ingresó nada para buscar.")

def busquedaVehiculo(request):
    return render(request, "aplicacion/buscarVehiculo.html")

def buscarVehiculo(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        vehiculos = Vehiculo.objects.filter(nombre__icontains=patron)
        contexto = {"vehiculos": vehiculos, 'titulo': f'Patrón de búsqueda:"{patron}"'}
        return render(request, "aplicacion/vehiculos.html", contexto)
    return HttpResponse("No se ingresó nada para buscar.")

def busquedaProducto(request):
    return render(request, "aplicacion/buscarProducto.html")

def buscarProducto(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        productos = Producto.objects.filter(nombre__icontains=patron)
        contexto = {"productos": productos, 'titulo': f'Patrón de búsqueda:"{patron}"'}
        return render(request, "aplicacion/productos.html", contexto)
    return HttpResponse("No se ingresó nada para buscar.")
