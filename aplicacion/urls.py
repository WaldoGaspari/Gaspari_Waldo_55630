from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home" ),
    path('servicios/', ServicioList.as_view(), name="servicios" ),
    path('create_servicio/', ServicioCreate.as_view(), name="create_servicio" ),
    path('update_servicio/<int:pk>/', ServicioUpdate.as_view(), name="update_servicio" ),
    path('delete_servicio/<int:pk>/', ServicioDelete.as_view(), name="delete_servicio" ),
    path('vehiculos/', VehiculoList.as_view(), name="vehiculos" ),
    path('create_vehiculo/', VehiculoCreate.as_view(), name="create_vehiculo" ),
    path('update_vehiculo/<int:pk>/', VehiculoUpdate.as_view(), name="update_vehiculo" ),
    path('delete_vehiculo/<int:pk>/', VehiculoDelete.as_view(), name="delete_vehiculo" ),
    path('productos/', ProductoList.as_view(), name="productos" ),
    path('create_producto/', ProductoCreate.as_view(), name="create_producto" ),
    path('update_producto/<int:pk>/', ProductoUpdate.as_view(), name="update_producto" ),
    path('delete_producto/<int:pk>/', ProductoDelete.as_view(), name="delete_producto" ),
    path('login/', loguearse, name="login" ),
    path('registro/', registrarse, name="registro" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('editar_usuario/', editarUsuario, name="editar_usuario" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),
]