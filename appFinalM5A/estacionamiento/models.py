from django.db import models
from djongo import models
from django import forms

# Create your models here.
class tipo_vehiculo(models.Model):
    codigo_tipo = models.CharField(max_length=10) #textos largos
    descripcion = models.CharField(max_length=50)
    activo=models.BooleanField(default=True)
class plazas(models.Model):
    codigo_plaza=models.CharField(max_length=10)
    descripcion_plaza=models.CharField(max_length=50)
    estado_plaza=models.BooleanField()
    activo=models.BooleanField(default=True)
class tarifas(models.Model):
    cod_tarifa=models.CharField(max_length=10)
    tiempo_tarifa=models.CharField(max_length=10)
    precio_tarifa=models.CharField(max_length=10)
    activo = models.BooleanField(default=True)

class usuarios(models.Model):
    id_usuario=models.CharField(max_length=20)
    nombre_usuario= models.CharField(max_length=100)
    clave_usuario=models.CharField(max_length=100)
    correo_usuario=models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

class historial_usuarios(models.Model):
    id_historial_us=models.CharField(max_length=20)
    fecha_registro=models.DateTimeField(auto_now_add=True)
    usuario=models.EmbeddedField(model_container=usuarios)

class roles(models.Model):
    cod_rol=models.CharField(max_length=10, unique=True)
    nombre_rol=models.CharField(max_length=10)
    activo = models.BooleanField(default=True)

class administradores(models.Model):
    id_admin=models.CharField(max_length=10)
    id_rol=models.EmbeddedField(
        model_container=roles
    )
    activo = models.BooleanField(default=True)

class cliente(models.Model):
    id_cliente=models.CharField(max_length=20)
    nombre_completo=models.CharField(max_length=30)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

class vehiculo(models.Model):
    id_vehiculo=models.CharField(max_length=20)
    id_placa_vehiculo=models.CharField(max_length=20)
    id_propietario=models.CharField(max_length=20)
    hora_entrada=models.DateTimeField(auto_now_add=True)
    hora_salida=models.DateTimeField(null=True)
    tipo_vehiculo=models.EmbeddedField(
        model_container=tipo_vehiculo
    )
    plaza_usada=models.EmbeddedField(
        model_container=plazas
    )
    activo=models.BooleanField(default=True)
    tiempo_transcurrido=models.IntegerField(null=True)
class vehiculo1(models.Model):
    id_placa_vehiculo = models.CharField(max_length=20)
    id_propietario = models.CharField(max_length=20)
    hora_entrada = models.DateTimeField(auto_now_add=True)
    hora_salida = models.DateTimeField(null=True)
    tipo_vehiculo = models.CharField(max_length=20)
    plaza_usada = models.CharField(max_length=20)
    activo=models.BooleanField(default=True)
    facturada=models.BooleanField(default=False)
class ticket(models.Model):
    id_ticket=models.CharField(max_length=20)
    fecha_emision=models.DateTimeField(auto_now_add=True)
    valor_pagar=models.CharField(max_length=20)
    vehiculo=models.EmbeddedField(model_container=vehiculo)

class ticket1(models.Model):
    fecha_emision=models.DateTimeField(auto_now_add=True)
    valor_pagar=models.CharField(max_length=20)
    vehiculo=models.CharField(max_length=20)
    activo = models.BooleanField(default=True)






