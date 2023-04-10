from django import forms
from .models import Perfil

# Define your forms here.

class PerfilForm(forms.ModelForm):
    """
        DOCSTRING: PerfilForm, responsable de la actualizacion de perfiles de usuario
    """
    class Meta:
        model = Perfil
        fields = ['foto_de_perfil', 'carrera', 'siguiendo']