from rest_framework import serializers
from .models import Archivo

# Define your serializers here.


class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields = ['archivo', 'creado_por']

