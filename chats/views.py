from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import MensajeSerializer
from grupos.models import Grupo
from .models import Mensaje
from .forms import MensajeForm

# Create your views here.


class MensajeAPIView(APIView):
    """
        DOCSTRING: NotificacionesAPIView, APIView responsable de manejar las notificaciones por usuario
    """

    serializer = MensajeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        try:
            # Recolectar Grupo
            grupo = Grupo.objects.get(pk=pk)
            # Recolectar Usuario
            mensajes = Mensaje.objects.filter(grupo=grupo)
            # Serializar Usuario
            data = self.serializer(mensajes, many=True).data
            # Retornar Usuario
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la extraccion de mensajes'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, pk=None):
        try:
            # Recolectar Usuario
            usuario = request.user
            # Recolectar Grupo
            grupo = Grupo.objects.get(pk=pk)
            # Validar datos
            mensaje_form = MensajeForm(request.data)
            if mensaje_form.is_valid():
                mensaje = mensaje_form.save(commit=False)
                mensaje.grupo = grupo
                mensaje.usuario = usuario
                mensaje.save()
                mensaje_serializado = self.serializer(mensaje).data
                return Response({'data': mensaje_serializado}, status=status.HTTP_200_OK)
            return Response({'error': 'El mensaje no ha podido ser enviado'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la extracciond de mensajes'}, status=status.HTTP_200_OK)
