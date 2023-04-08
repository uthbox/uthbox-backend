from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Grupo(models.Model):
    """
        DOCSTRING: Grupo, clase responsable del agrupamiento de usuarios que comparten dicho grupo, permitiendo la interaccion
        entre ellos.
    """
    nombre = models.CharField('Nombre de Grupo', max_length=100, blank=False, null=False, default=None)
    usuarios = models.ManyToManyField(User, related_name='grupos', blank=True, default=None)
    activo = models.BooleanField(blank=False, null=False, default=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre