from rest_framework import serializers
from autenticacion.serializers import UTHUsuarioSerializer
from .models import Notificacion

# Define your serializers here.

class NotificacionSerializer(serializers.ModelSerializer):

    usuario_creador = UTHUsuarioSerializer()

    class Meta:
        model = Notificacion
        fields = ['titulo', 'mensaje', 'fecha', 'usuario_creador']