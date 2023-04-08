from rest_framework import serializers
from autenticacion.serializers import UTHUsuarioSerializer
from .models import Grupo

# Define your serializers here.


class GrupoSerializer(serializers.ModelSerializer):

    usuarios = UTHUsuarioSerializer(many=True)

    class Meta:
        model = Grupo
        fields = ['id', 'nombre', 'usuarios']

