from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your serializers here.

class UTHUsuarioSerializer(serializers.ModelSerializer):
    """
        DOCSTRING: UTHUsuarioSerializer responsable de la conversion de instancias de UTHUsuario entre tipos.
    """

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password1', 'password2']
