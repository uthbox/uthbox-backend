from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UTHUsuario(AbstractUser):
    """
        DOCSTRING: UTHUsuario, clase responsable de la autenticacion de usuarios.
    """
    first_name = models.CharField(max_length=30, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=30, blank=True, null=True, default=None)
    email = models.EmailField(blank=True, null=True, default=None)


class CodigosVerificacion(models.Model):
    """
        DOCSTRING: UTHUsuario, clase responsable de la autenticacion de usuarios.
    """
    codigo = models.CharField(max_length=6, blank=False, null=True, default=None)
    usuario = models.ForeignKey(UTHUsuario, on_delete=models.CASCADE, blank=False, null=False, default=None)