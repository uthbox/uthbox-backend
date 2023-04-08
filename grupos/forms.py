from django import forms
from .models import Grupo

# Define your forms here.

class GrupoForm(forms.ModelForm):
    """
        DOCSTRING: formulario responsable de la creacion y actualizacion de grupos
    """
    class Meta:
        model = Grupo
        fields = ['nombre', 'usuarios']