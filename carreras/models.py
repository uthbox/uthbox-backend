from django.db import models

# Create your models here.


class Carrera(models.Model):

    """
        DOCSTRING: Carrera, clase responsable de las carreras universitarias ofrecidas.
    """

    nombre_carrera = models.CharField(max_length=255, blank=False, null=False, default=None)

    def save(self, *args, **kwargs):
        self.nombre_carrera = self.nombre_carrera.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_carrera
    