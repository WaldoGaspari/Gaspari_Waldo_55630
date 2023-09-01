from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


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

class ServicioList(ListView):
    model = Servicio

class ServicioCreate(CreateView):
    model = Servicio
    fields = ['nombre', 'tipo', 'descripcion']
    success_url = reverse_lazy('servicios')

class ServicioUpdate(UpdateView):
    model = Servicio
    fields = ['nombre', 'tipo', 'descripcion']
    success_url = reverse_lazy('servicios')

class ServicioDelete(DeleteView):
    model = Servicio
    success_url = reverse_lazy('servicios')

class VehiculoList(ListView):
    model = Vehiculo

class VehiculoCreate(CreateView):
    model = Vehiculo
    fields = ['marca', 'modelo', 'tipo']
    success_url = reverse_lazy('vehiculos')

class VehiculoUpdate(UpdateView):
    model = Vehiculo
    fields = ['marca', 'modelo', 'tipo']
    success_url = reverse_lazy('vehiculos')

class VehiculoDelete(DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('vehiculos')

class ProductoList(ListView):
    model = Producto

class ProductoCreate(CreateView):
    model = Producto
    fields = ['nombre', 'marca', 'uso']
    success_url = reverse_lazy('productos')

class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['nombre', 'marca', 'uso']
    success_url = reverse_lazy('productos')

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')
