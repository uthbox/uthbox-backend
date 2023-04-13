from django.urls import path
from .views import Autenticacion, Registro, VerificacionAPIView

# Define your urls here.

urlpatterns = [
    path('', Autenticacion.as_view(), name='autenticacion'),
    path('registro/', Registro.as_view(), name='cuentas'),
    path('verificacion/<int:pk>', VerificacionAPIView.as_view(), name='verificacion'),
]