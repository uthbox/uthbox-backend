from rest_framework import serializers
from autenticacion.serializers import UTHUsuarioSerializer
from carreras.serializers import CarreraSerializer
from .models import Perfil, Relaciones

# Define your serializers here.

class PerfilSerializer(serializers.ModelSerializer):

    usuario = UTHUsuarioSerializer()
    carrera = CarreraSerializer()
    siguiendo = serializers.SerializerMethodField()

    class Meta:
        model = Perfil
        fields = ['id', 'foto_de_perfil', 'siguiendo', 'carrera', 'verificado', 'usuario']

    def get_siguiendo(self, obj):
        relaciones = Relaciones.objects.filter(usuario_siguiendo=obj)
        return RelacionesSerializer(relaciones, many=True).data


class RelacionesSerializer(serializers.ModelSerializer):

    usuario_seguido = PerfilSerializer()

    class Meta:
        model = Relaciones
        fields = ['usuario_seguido']