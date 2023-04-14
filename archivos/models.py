from django.db import models
from django.contrib.auth import get_user_model
from grupos.models import Grupo

User = get_user_model()

# Create your models here.

class Archivo(models.Model):
    """
        DOCSTRING: Archivo, clase responsable del alojamiento de archivos y vinculo a un grupo en especifico, contiene una relacion
        de uno a uno con la clase Grupo
    """
    archivo = models.FileField(upload_to='archivos', blank=False, null=False, default=None)
    grupo = models.OneToOneField(Grupo, on_delete=models.CASCADE, blank=False, null=False)
    activo = models.BooleanField(blank=False, null=False, default=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, default=None)

    def __str__(self):
        return self.archivo.name