from rest_framework import serializers
from autenticacion.serializers import UTHUsuarioSerializer
from carreras.serializers import CarreraSerializer
from .models import Perfil, Relaciones

# Define your serializers here.

class PerfilSerializer(serializers.ModelSerializer):

    usuario = UTHUsuarioSerializer()
    carrera = CarreraSerializer()

    class Meta:
        model = Perfil
        fields = ['id', 'foto_de_perfil', 'carrera', 'verificado', 'usuario']


class RelacionesSerializer(serializers.ModelSerializer):

    usuario_seguido = PerfilSerializer()

    class Meta:
        model = Relaciones
        fields = ['usuario_seguido']