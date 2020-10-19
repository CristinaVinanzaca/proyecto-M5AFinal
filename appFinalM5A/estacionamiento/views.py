from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from estacionamiento.models import administradores,plazas,roles,usuarios,vehiculo1,tipo_vehiculo,cliente,historial_usuarios,tarifas,ticket1
from estacionamiento.serializers import plazasSerializer,tipo_vehiculoSerializer,RolesSerializer,TarifasSerializer,ClienteSerializer,\
    UsuariosSerializer,AdministradoresSerializer, VehiculoSerializer, TicketSerializer

# Create your views here.
def plazas1 (request):
    plazasList = plazas.objects.all()
    return render(request,'plazas.html',{
        'titulo':'Lista de plazas',
        'plazas': plazasList
    })
def tipo_vehi (request):
    tvehiList = tipo_vehiculo.objects.all()
    return render(request,'tipo_vehiculo.html',{
        'titulo':'Lista de tipos de vehiculos',
        'tvehiList': tvehiList
    })
def usuarios1 (request):
    usuariosList = usuarios.objects.all()
    return render(request,'usuarios.html',{
        'titulo':'Lista de Usuarios',
        'usuariosList': usuariosList
    })
def roles1 (request):
    rolesList = roles.objects.all()
    return render(request,'roles.html',{
        'titulo':'Lista de roles',
        'rolesList': rolesList
    })

def clientes1 (request):
    clientesList = cliente.objects.all()
    return render(request,'clientes.html',{
        'titulo':'Lista de clientes',
        'clientesList': clientesList
    })

def tarifas1 (request):
    tarifasList = tarifas.objects.all()
    return render(request,'tarifas.html',{
        'titulo':'Tarifas Existentes',
        'tarifasList': tarifasList
    })
def create_cliente (request):
    return render(request,'clienteNuevo.html',{
        'titulo':'Ingresar Cliente'
    })
def create_plaza (request):
    return render(request,'plazaNUeva.html',{
        'titulo':'Ingresar Plazas'
    })

def create_rol (request):
    return render(request,'rolNuevo.html',{
        'titulo':'Ingresar Rol'
    })
def create_tipoVehi (request):
    return render(request,'nievoTipoVehi.html',{
        'titulo':'Ingresar Nuevo Tipo de Vehiculo'
    })
def create_user (request):
    usuariosList = usuarios.objects.all()
    return render(request,'nuevoUsuario.html',{
        'titulo':'Ingresar Nuevo Usuario',
        'usuariosList': usuariosList
    })
def create_tarifa (request):
    return render(request,'nuevaTarifa.html',{
        'titulo':'Ingresar Nueva Tarifa'
    })

def vehiculos (request):
    vehiculos = vehiculo1.objects.all()
    return render(request,'vehiculos.html',{
        'titulo':'Lista de Vehiculos',
        'vehiculos': vehiculos
    })
def create_vehiculos (request):
    plazas_list=plazas.objects.all()
    tVehiculos=tipo_vehiculo.objects.all()
    return render(request,'IngresarVehiculo.html',{
        'titulo':'Ingreso de vehiculos nuevos',
        'plazas_list': plazas_list,
        'tVehiculos':tVehiculos,
    })
class plazasViewSet(ModelViewSet):
    serializer_class = plazasSerializer
    queryset = plazas.objects.all()

class tipoVehiViewSet(ModelViewSet):
    serializer_class = tipo_vehiculoSerializer
    queryset = tipo_vehiculo.objects.all()

class RolesViewSet(ModelViewSet):
    serializer_class = RolesSerializer
    queryset = roles.objects.all()

class TarifasViewSet(ModelViewSet):
    serializer_class = TarifasSerializer
    queryset = tarifas.objects.all()

class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = cliente.objects.all()
    filterset_fields = {
        'id_cliente': ['exact', 'icontains'],
    }
def login1(request):
    return render(request, 'login.html', {
        'titulo': 'Inicio de sesión',
    })
def home(request):
    return render(request, 'home.html', {
        'titulo': 'Home',
    })
def factura(request,id):
    ticket2=ticket1.objects.get(id=id)
    return render(request, 'factura.html', {
        'titulo': 'factura',
        'ticket':ticket2,
    })
class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuariosSerializer
    queryset = usuarios.objects.all()

class AdministradorViewSet(ModelViewSet):
    serializer_class = AdministradoresSerializer
    queryset = administradores.objects.all()

class VehiculoViewSet(ModelViewSet):
    serializer_class = VehiculoSerializer
    queryset = vehiculo1.objects.all()

class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = ticket1.objects.all()