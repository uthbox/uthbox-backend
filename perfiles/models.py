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


class Relaciones(models.Model):
    """
        DOCSTRING: Social, clase intermediaria para el manejo de relaciones sociales.
    """
    usuario_siguiendo = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=False, null=False, related_name='creador')
    usuario_seguido = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=False, null=False, related_name='blanco')

    def __str__(self):
        siguiendo_nombre = '{} {}'.format(self.usuario_siguiendo.usuario.first_name, self.usuario_siguiendo.usuario.last_name)
        seguido_nombre = '{} {}'.format(self.usuario_seguido.usuario.first_name, self.usuario_seguido.usuario.last_name)
        return '{} siguiendo a {}'.format(siguiendo_nombre, seguido_nombre)

