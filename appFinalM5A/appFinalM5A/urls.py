"""appFinalM5A URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from estacionamiento.views import plazas1,tipo_vehi,roles1,usuarios1,clientes1,tarifas1,create_cliente,create_plaza,create_rol,create_tipoVehi,create_user,create_tarifa, \
    vehiculos,create_vehiculos,login1,home,factura
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('estacionamiento.api')),
    path('plazas/',plazas1, name='plazas1'),
    path('tiposDeVehiculos/',tipo_vehi, name='tipo_vehi'),
    path('roles/',roles1, name='roles'),
    path('usuarios/',usuarios1, name='usuarios'),
    path('clientes/',clientes1, name='clientes'),
    path('tarifas/',tarifas1, name='tarifas'),
    path('nuevoCliente/',create_cliente, name='create_cliente'),
    path('nuevaPlaza/',create_plaza, name='create_plaza'),
    path('nuevaRol/',create_rol, name='create_rol'),
    path('nuevaTipoVehi/',create_tipoVehi, name='create_tipoVehi'),
    path('nuevoUuser/',create_user, name='create_user'),
    path('nuevoTarifa/',create_tarifa, name='create_tarifa'),
    path('vehiculos/',vehiculos, name='Lista_vehiculos'),
    path('create_vehiculo/',create_vehiculos, name='create_vehiculo'),
    path('login/',login1, name='loggin'),
    path('home/',home, name='home'),
    path('ticket/<int:id>',factura, name='ticket'),

]
