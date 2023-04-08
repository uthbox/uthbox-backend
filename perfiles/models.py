from django.db import models
from django.contrib.auth import get_user_model
from carreras.models import Carrera

Usuario = get_user_model()

# Create your models here.

class Perfil(models.Model):
    """
        DOCSTRING: Perfil, clase responsable del alojamiento de datos personales para la clase UTHUsuario, contiene una relacion
        de uno a uno con dicha clase.
    """
    foto_de_perfil = models.ImageField(upload_to='perfil', blank=True, null=True, default=None)
    carrera = models.ForeignKey(Carrera, blank=True, null=True, on_delete=models.CASCADE, default=None)
    verificado = models.BooleanField(blank=False, null=False, default=False)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return '{} {} - Perfil'.format(self.usuario.first_name, self.usuario.last_name)