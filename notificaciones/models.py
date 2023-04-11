from django.contrib.auth import get_user_model
from django.db import models

Usuario = get_user_model()

# Create your models here.

class Notificacion(models.Model):
    """
        DOCSTRING: Notificacion, responsable del alojamiento de notificaciones por usuario
    """
    titulo = models.CharField(max_length=255, blank=False, null=True, default=None)
    mensaje = models.CharField(max_length=255, blank=False, null=True, default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False, null=False, default=None)
    usuario_creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False, null=False, default=None, related_name='creador')


    def save(self, *args, **kwargs):
        self.titulo = self.titulo.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Notificacion para {} {}'.format(self.usuario.first_name, self.usuario.last_name)

