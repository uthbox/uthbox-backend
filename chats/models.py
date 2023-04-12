from django.db import models
from django.contrib.auth import get_user_model
from grupos.models import Grupo

Usuario = get_user_model()

# Create your models here.


class Mensaje(models.Model):
    """
        DOCSTRING: Carrera, clase responsable de las carreras universitarias ofrecidas.
    """

    mensaje = models.CharField(max_length=255, blank=False, null=False, default=None)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, blank=False, null=False, default=None)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False, null=False, default=None)

    def __str__(self):
        return "Mensaje de {} al grupo {}".format(self.usuario.username, self.grupo.nombre)