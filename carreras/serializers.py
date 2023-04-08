from rest_framework import serializers
from .models import Carrera

# Define your serializers here.

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'