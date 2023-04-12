from django import forms
from django.contrib.auth import get_user_model
from .models import Mensaje

# Create your models here.


class MensajeForm(forms.ModelForm):
    """
        DOCSTRING: MensajeForm, clase responsable de la creacion de mensajes
    """
    class Meta:
        model = Mensaje
        fields = ['mensaje']