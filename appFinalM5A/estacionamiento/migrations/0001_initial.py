# Generated by Django 2.2.11 on 2020-04-02 04:09

from django.db import migrations, models
import djongo.models.fields
import estacionamiento.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administradores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_admin', models.CharField(max_length=10, unique=True)),
                ('id_rol', djongo.models.fields.EmbeddedField(model_container=estacionamiento.models.roles, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.CharField(max_length=20, unique=True)),
                ('nombre_completo', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='historial_usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_historial_us', models.CharField(max_length=20, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('usuario', djongo.models.fields.EmbeddedField(model_container=estacionamiento.models.usuarios, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='plazas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_plaza', models.CharField(max_length=10, unique=True)),
                ('descripcion_plaza', models.CharField(max_length=50)),
                ('estado_plaza', models.BooleanField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_rol', models.CharField(max_length=10, unique=True)),
                ('nombre_rol', models.CharField(max_length=10)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='tarifas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_tarifa', models.CharField(max_length=10, unique=True)),
                ('tiempo_tarifa', models.CharField(max_length=10)),
                ('precio_tarifa', models.CharField(max_length=10)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ticket', models.CharField(max_length=20, unique=True)),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('valor_pagar', models.CharField(max_length=20)),
                ('vehiculo', djongo.models.fields.EmbeddedField(model_container=estacionamiento.models.vehiculo, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_tipo', models.CharField(max_length=10, unique=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=20, unique=True)),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('clave_usuario', models.CharField(max_length=100)),
                ('correo_usuario', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_vehiculo', models.CharField(max_length=20, unique=True)),
                ('id_placa_vehiculo', models.CharField(max_length=20)),
                ('id_propietario', models.CharField(max_length=20)),
                ('hora_entrada', models.DateTimeField(auto_now_add=True)),
                ('hora_salida', models.DateTimeField(null=True)),
                ('tipo_vehiculo', djongo.models.fields.EmbeddedField(model_container=estacionamiento.models.tipo_vehiculo, null=True)),
                ('plaza_usada', djongo.models.fields.EmbeddedField(model_container=estacionamiento.models.plazas, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('tiempo_transcurrido', models.IntegerField(null=True)),
            ],
        ),
    ]