from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "aplicacion/inicio.html")

@login_required
def servicios(request):
    contexto = {'servicios': Servicio.objects.all()}
    return render(request, "aplicacion/servicios.html", contexto)

@login_required
def vehiculos(request):
    contexto = {'vehiculos': Vehiculo.objects.all()}
    return render(request, "aplicacion/vehiculos.html", contexto)

@login_required
def productos(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, "aplicacion/productos.html", contexto)

@login_required
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

@login_required
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

@login_required
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

@login_required
def busquedaServicio(request):
    return render(request, "aplicacion/buscarServicio.html")

@login_required
def buscarServicio(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        servicios = Servicio.objects.filter(nombre__icontains=patron)
        contexto = {"servicios": servicios, 'titulo': f'Patrón de búsqueda:"{patron}"'}
        return render(request, "aplicacion/servicios.html", contexto)
    return HttpResponse("No se ingresó nada para buscar.")

@login_required
def busquedaVehiculo(request):
    return render(request, "aplicacion/buscarVehiculo.html")

@login_required
def buscarVehiculo(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        vehiculos = Vehiculo.objects.filter(nombre__icontains=patron)
        contexto = {"vehiculos": vehiculos, 'titulo': f'Patrón de búsqueda:"{patron}"'}
        return render(request, "aplicacion/vehiculos.html", contexto)
    return HttpResponse("No se ingresó nada para buscar.")

@login_required
def busquedaProducto(request):
    return render(request, "aplicacion/buscarProducto.html")

@login_required
def buscarProducto(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        productos = Producto.objects.filter(nombre__icontains=patron)
        contexto = {"productos": productos, 'titulo': f'Patrón de búsqueda:"{patron}"'}
        return render(request, "aplicacion/productos.html", contexto)
    return HttpResponse("No se ingresó nada para buscar.")

def loguearse(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido al sitio {usuario}!'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos.'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos.'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm})

def registrarse(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm})
