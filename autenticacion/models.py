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
