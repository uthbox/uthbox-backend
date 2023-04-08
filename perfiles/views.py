from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
from autenticacion.forms import UTHUsuarioForm
from .serializers import PerfilSerializer
from .models import Perfil
from .forms import PerfilForm

User = get_user_model()

# Create your views here.

class PerfilAPIView(APIView):
    """
        DOCSTRING: Perfil, APIView responsable de manejar toda la logica relacionada perfiles y usuarios
    """

    serializer = PerfilSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Recolectar Usuario
            perfil = Perfil.objects.get(usuario=request.user)
            # Serializar Usuario
            perfil_data = PerfilSerializer(perfil).data
            # Retornar Usuario
            return Response({'data': perfil_data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Perfil no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        try:
            # Recolectar Datos
            data = request.data
            # Recolectar Instancia
            perfil = Perfil.objects.get(usuario=request.user)
            usuario = User.objects.get(pk=request.user.pk)
            # Validar Datos
            perfil_form = PerfilForm(data, instance=perfil)
            usuario_form = UTHUsuarioForm(data, instance=usuario)
            if usuario_form.is_valid() and perfil_form.is_valid():
                usuario_form.save()
                perfil_form.save()
                return Response({'data': PerfilSerializer(perfil).data},  status=status.HTTP_200_OK)
            else:
                return Response({'error': usuario_form.errors},  status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Error al actualizar el usuario'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            # Recolectar usuario para desactivar
            usuario = User.objects.get(pk=request.user.pk)
            # Desactivar usuario
            usuario.is_active = False
            # Save user
            usuario.save()
            # Regresar usuario
            return Response({'data': 'Usuario desactivado exitosamente'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error al desactivar el usuario'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PerfilesFiltroAPIView(APIView):
    """
        DOCSTRING: Perfil, APIView responsable de filtrar perfiles y usuarios
    """

    serializer = PerfilSerializer

    def get(self, request):
        try:
            # Recolectar query parameters
            busqueda = request.query_params.get('busqueda')
            # Busqueda de Perfiles
            perfiles = Perfil.objects.filter(Q(usuario__username__icontains=busqueda) | Q(usuario__email__icontains=busqueda))
            resutlado = PerfilSerializer(perfiles, many=True).data
            return Response({'data': resutlado}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error al filtrar perfiles'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PerfilesAPIView(APIView):
    """
        DOCSTRING: Perfil, APIView responsable de manejar toda la logica relacionada perfiles y usuarios
    """

    serializer = PerfilSerializer

    def get(self, request, pk=None):
        try:
            if pk:
                resultado = Perfil.objects.get(pk=pk)
            else:
                resultado = Perfil.objects.all()
            data = PerfilSerializer(resultado, many=pk is None).data
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error al recolectar resultado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
