from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

User = get_user_model()

# Define your forms here.


class UTHUsuarioCreacionForm(UserCreationForm):
    """
        DOCSTRING: Formulario responsable de la creacion y validacion de contraseñas en el registro de un usuario.
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class UTHUsuarioForm(UserChangeForm):
    """
        DOCSTRING: Formulario responsable de la actualizacion de usuarios.
    """

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UTHUsuarioCambiarContrasenaForm(PasswordChangeForm):
    """
        DOCSTRING: Formulario responsable de la actualizacion de contraseña.
    """
    pass