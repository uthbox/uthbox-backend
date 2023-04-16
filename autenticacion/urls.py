from django.urls import path
from .views import Autenticacion, Registro, VerificacionAPIView, \
                   CambiarContrasenaAPIView, GenerarCodigoDeVerificacionAPIView, \
                   VerificarCodigoAPIView, RestaurarContrasenaAPIView

# Define your urls here.

urlpatterns = [
    path('', Autenticacion.as_view(), name='autenticacion'),
    path('registro/', Registro.as_view(), name='cuentas'),
    path('verificacion/<int:pk>', VerificacionAPIView.as_view(), name='verificacion'),
    path('cambiar_contra/', CambiarContrasenaAPIView.as_view(), name='cambiar_contra'),
    path('solicitar_restauracion/', GenerarCodigoDeVerificacionAPIView.as_view(), name='solicitar_restauracion'),
    path('verificar_codigo/', VerificarCodigoAPIView.as_view(), name='verificar_codigo'),
    path('restaurar_contra/', RestaurarContrasenaAPIView.as_view(), name='restaurar_contra'),
]