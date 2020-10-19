from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS
from estacionamiento.models import administradores,plazas,roles,usuarios,vehiculo1,tipo_vehiculo,cliente,historial_usuarios,tarifas,ticket1

class plazasSerializer(serializers.ModelSerializer):
    class Meta:
        model = plazas
        fields = ALL_FIELDS
    def create(self, validated_data):
        plazas1=plazas(**validated_data)
        plazas1.save()
        return plazas1

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            instance.__setattr__(key, value)
        instance.save()
        return instance

class tipo_vehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model=tipo_vehiculo
        fields=ALL_FIELDS
    def create(self, validated_data):
        tipo_vehi=tipo_vehiculo(**validated_data)
        tipo_vehi.save()
        return tipo_vehi
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            instance.__setattr__(key, value)
        instance.save()
        return instance

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model=roles
        fields=ALL_FIELDS
    def create(self, validated_data):
        rol=roles(**validated_data)
        rol.save()
        return rol
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            instance.__setattr__(key, value)
        instance.save()
        return instance

class TarifasSerializer(serializers.ModelSerializer):
    class Meta:
        model=tarifas
        fields=ALL_FIELDS
    def create(self, validated_data):
        tarifa=tarifas(**validated_data)
        tarifa.save()
        return tarifa
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            instance.__setattr__(key, value)
        instance.save()
        return instance

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=cliente
        fields=ALL_FIELDS
    def create(self, validated_data):
        cliente1=cliente(**validated_data)
        cliente1.save()
        return cliente1
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            instance.__setattr__(key, value)
        instance.save()
        return instance

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model=vehiculo1
        fields=ALL_FIELDS
    def create(self, validated_data):
        vehiculo=vehiculo1(**validated_data)
        vehiculo.save()
        return vehiculo
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            instance.__setattr__(key, value)
        instance.save()
        return instance

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=ticket1
        fields=ALL_FIELDS
    def create(self, validated_data):
        ticket=ticket1(**validated_data)
        ticket.save()
        return ticket
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            instance.__setattr__(key, value)
        instance.save()
        return instance

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model=usuarios
        fields=ALL_FIELDS
    def create(self, validated_data):
        usuario=usuarios(**validated_data)
        usuario.save()
        return usuario
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            instance.__setattr__(key, value)
        instance.save()
        return instance

class AdministradoresSerializer(serializers.ModelSerializer):
    id_rol=RolesSerializer()

    class Meta:
        model = administradores
        fields = ALL_FIELDS

    def create(self, validated_data):
        rol = validated_data.pop('id_rol')
        rol_obj=roles(**rol)
        print('ROL:',rol_obj.cod_rol )
        admin=administradores(**validated_data)
        admin.id_rol=rol_obj
        admin.save()
        return admin
    def update(self, instance, validated_data):
        rol = validated_data.pop('id_rol')
        rol_obj = roles(**rol)
        for key, value in validated_data.items():
            instance.__setattr__(key,value)
        instance.id_rol = rol_obj
        instance.save()
        return instance
