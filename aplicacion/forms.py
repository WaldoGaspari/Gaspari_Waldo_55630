from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)