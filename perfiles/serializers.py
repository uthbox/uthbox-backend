from rest_framework import serializers
from autenticacion.serializers import UTHUsuarioSerializer
from carreras.serializers import CarreraSerializer
from .models import Perfil

# Define your serializers here.


class PerfilSerializer(serializers.ModelSerializer):

    usuario = UTHUsuarioSerializer()
    carrera = CarreraSerializer()

    class Meta:
        model = Perfil
        fields = ['foto_de_perfil', 'carrera', 'verificado', 'usuario']