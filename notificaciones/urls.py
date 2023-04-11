from django.urls import path
from .views import NotificacionesAPIView

# Define your urls here.

urlpatterns = [
    path('', NotificacionesAPIView.as_view(), name='notificaciones')
]