from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
from autenticacion.forms import UTHUsuarioForm
from .serializers import NotificacionSerializer
from .models import Notificacion

# Create your views here.


class NotificacionesAPIView(APIView):
    """
        DOCSTRING: NotificacionesAPIView, APIView responsable de manejar las notificaciones por usuario
    """

    serializer = NotificacionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Recolectar Usuario
            notificaciones = Notificacion.objects.filter(usuario=request.user)
            # Serializar Usuario
            data = self.serializer(notificaciones, many=True).data
            # Retornar Usuario
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Perfil no encontrado'}, status=status.HTTP_404_NOT_FOUND)
