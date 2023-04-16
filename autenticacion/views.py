from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from utilities.mailing import enviar_verificacion, enviar_codigo
from utilities.authentication import generar_codigo
from perfiles.models import Perfil
from perfiles.serializers import PerfilSerializer
from carreras.models import Carrera
from .models import CodigosVerificacion
from .serializers import UTHUsuarioSerializer
from .forms import UTHUsuarioCreacionForm, UTHUsuarioForm, UTHUsuarioCambiarContrasenaForm
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
            perfil = Perfil.objects.get(usuario__username=usuario)
            if not perfil.verificado:
                return Response({'error': 'Usuario aun no verificado.'}, status=status.HTTP_400_BAD_REQUEST)
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
                enviar_verificacion(user.email, user.id)
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


class VerificacionAPIView(APIView):
    """
        DOCSTRING: VerificacionAPIView, APIView responsable de la verificacion de identidad de usuarios.
    """
    def get(self, request, pk=None):
        try:
            # Recoleccion del usuario
            perfil = Perfil.objects.get(usuario__pk=pk)
            # Verificacion de Usuario
            perfil.verificado = True
            perfil.save()
            # Respuesta del APIView
            return HttpResponse("Usuario verificado! Sientase libre de cerrar esta pestaña y disfrutar de nuestra aplicacion.")
        except:
            return HttpResponse("Ocurrio un error en la verificacion de este usuario.")


class CambiarContrasenaAPIView(APIView):
    """
        DOCSTRING: CambiarContrasenaAPIView, APIView responsable de la actualizacion de contraseña.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
        DOCSTRING: CambiarContrasenaAPIView, APIView responsable de la actualizacion de contrasenas.
    """
    def post(self, request):
        try:
            contra_form = UTHUsuarioCambiarContrasenaForm(request.user, request.data)
            if contra_form.is_valid():
                contra_form.save()
                return Response({'data': 'Contraseña actualizada correctamente!'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': contra_form.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Error al intentar cambiar la contraseña'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GenerarCodigoDeVerificacionAPIView(APIView):
    """
        DOCSTRING: GenerarCodigoDeVerificacionAPIView, APIView responsable de la generacion de email con codigo de verificacion.
    """
    def post(self, request):
        # try:
            # Recolectar payload
            correo = request.data.get('email')
            # Recolectar usuario con email
            usuario = User.objects.get(email=correo)
            # Validar existencia del usuario
            if usuario:
                codigo = generar_codigo()
                CodigosVerificacion.objects.create(codigo=codigo, usuario=usuario)
                enviar_codigo(codigo, correo)
                return Response({'data': 'El codigo de verifiacion ha sido enviado a su correo'}, status=status.HTTP_200_OK)
            return Response({'error': 'Email no registrado'}, status=status.HTTP_400_BAD_REQUEST)
        # except:
        #     return Response({'error': 'Error al crear codigo de verificacion'}, status=status.HTTP_400_BAD_REQUEST)


class VerificarCodigoAPIView(APIView):
    """
        DOCSTRING: GenerarCodigoDeVerificacionAPIView, APIView responsable de la generacion de email con codigo de verificacion.
    """
    serializer = UTHUsuarioSerializer

    def post(self, request):
        try:
            # Recolectar payload
            codigo_enviado = request.data.get('codigo')
            # Recolectar codigo
            codigo_verificado = CodigosVerificacion.objects.get(codigo=codigo_enviado)
            # Validar existencia del usuario
            if codigo_verificado:
                return Response({'data': self.serializer(codigo_verificado.usuario).data}, status=status.HTTP_200_OK)
            return Response({'error': 'Este codigo no esta vinculado con ninguna solicitud de restauracion'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Error en la verificacion de codigo'}, status=status.HTTP_400_BAD_REQUEST)


class RestaurarContrasenaAPIView(APIView):
    """
        DOCSTRING: RestaurarContrasenaAPIView, APIView responsable de la actualizacion de contraseña.
    """
    def post(self, request):
        try:
            # Recolectar payload
            nueva_contra = request.data.get('contra')
            id_usuario = request.data.get('id')
            # Recolectar usuario
            usuario = User.objects.get(id=id_usuario)
            usuario.set_password(nueva_contra)
            usuario.save()
            # Validar existencia del usuario
            return Response({'data': 'Contraseña restaurada exitosamente'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error la restauracion de la contraseña'}, status=status.HTTP_400_BAD_REQUEST)



