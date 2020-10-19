from rest_framework import routers
from .views import plazasViewSet,tipoVehiViewSet,RolesViewSet,TarifasViewSet,ClienteViewSet,UsuarioViewSet,AdministradorViewSet, TicketViewSet,VehiculoViewSet
router = routers.DefaultRouter()
router.register(r'plazas', plazasViewSet)
router.register(r'TipoVehi', tipoVehiViewSet)
router.register(r'Roles', RolesViewSet)
router.register(r'Tarifas', TarifasViewSet)
router.register(r'Cliente', ClienteViewSet)
router.register(r'Usuario', UsuarioViewSet)
router.register(r'Admin', AdministradorViewSet)
router.register(r'Vehiculo', VehiculoViewSet)
router.register(r'Ticket', TicketViewSet)
urlpatterns = router.urls
