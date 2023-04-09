from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from perfiles.models import Perfil
from carreras.models import Carrera
from .serializers import UTHUsuarioSerializer
from .forms import UTHUsuarioCreacionForm, UTHUsuarioForm

User = get_user_model()


# Create your views here.

class Autenticacion(APIView):
    """
        DOCSTRING: Autenticacion, APIView responsable de manejar toda la logica relacionada con autenticacion de usuarios
        y generacion de tokens.
    """
    serializer = UTHUsuarioSerializer

    def post(self, request):
        try:
            # Recoleccion de datos
            usuario = request.data['username']
            contrasena = request.data['password']
            autenticado = authenticate(request, username=usuario, password=contrasena)
            if autenticado is not None:
                token, _ = Token.objects.get_or_create(user=autenticado)
                return Response({'data': {'token': token.key}}, status=status.HTTP_200_OK)
            return Response({'error': 'Credenciales Incorrectas.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error', 'Ocurrio un error al intentar autenticar el usuario.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Registro(APIView):
    """
        DOCSTRING: Registro, APIView responsable de la creacion de usuarios.
    """
    serializer = UTHUsuarioSerializer

    def post(self, request):
        try:
            # Crear usuario
            form_usuario = UTHUsuarioCreacionForm(request.data)
            # Validar usuario
            if form_usuario.is_valid():
                user = form_usuario.save()
                carrera = Carrera.objects.get(id=int(request.data['carrera']))
                Perfil.objects.create(usuario=user, carrera=carrera)
                return Response({'data': self.serializer(user).data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': form_usuario.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
                return Response({'error': 'Error en la creacion del usuario'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Usuarios(APIView):
    """
        DOCSTRING: Usuarios, APIView responsable de manejar toda la logica relacionada con usuarios.
    """

    serializer = UTHUsuarioSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Recoleccion de todos los usuarios
            usuario = User.objects.get(pk=request.user.pk)
            # Serializacion de todos los usuarios
            usuarios_serializados = self.serializer(usuario).data
            # Respuesta del APIView
            return Response({'data': usuarios_serializados}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la recoleccion de usuarios'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        try:
            # Recoleccion de usuario
            usuario = User.objects.get(pk=request.user.pk)
            # Recoleccion de la informacion
            usuario_form = UTHUsuarioForm(request.data, instance=usuario)
            # Guardar cambios de Usuario
            if usuario_form.is_valid():
                usuario = usuario_form.save()
            else:
                return Response({'error': usuario_form.errors}, status=status.HTTP_400_BAD_REQUEST)
            # Respuesta del APIView
            return Response({'data':  self.serializer(usuario).data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la actualizacion usuario'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            # Recoleccion del usuario
            usuario = User.objects.get(pk=request.user.pk)
            # Desactivacion del usuario
            usuario.is_active = False
            usuario.save()
            # Respuesta del APIView
            return Response({'data': 'Usuario desactivado exitosamente'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la desactivacion del usuario'}, status=status.HTTP_400_BAD_REQUEST)
