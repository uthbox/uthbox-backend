from rest_framework import serializers
from autenticacion.serializers import UTHUsuarioSerializer
from .models import Mensaje

# Define your serializers here.

class MensajeSerializer(serializers.ModelSerializer):

    usuario = UTHUsuarioSerializer()

    class Meta:
        model = Mensaje
        fields = ['mensaje', 'usuario']
