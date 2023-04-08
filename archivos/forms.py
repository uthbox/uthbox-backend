from django import forms
from .models import Archivo

# Define your forms here.


class ArchivoForm(forms.ModelForm):
    """
        DOCSTRING: formulario responsable de la creacion y actualizacion de archivos
    """
    class Meta:
        model = Archivo
        fields = ['archivo', 'grupo']

