from django import forms

class FormularioServicio(forms.Form):
    nombre = forms.CharField(max_length=30, required=True)
    tipo = forms.CharField(max_length=10, required=True)
    descripcion = forms.CharField(max_length=200, required=True)

class FormularioVehiculo(forms.Form):
    marca = forms.CharField(max_length=30, required=True)
    modelo = forms.CharField(max_length=30, required=True)
    tipo = forms.CharField(max_length=20, required=True)

class FormularioProducto(forms.Form):
    nombre = forms.CharField(max_length=30, required=True)
    marca = forms.CharField(max_length=30, required=True)
    uso = forms.CharField(max_length=60, required=True)
    