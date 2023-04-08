from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from grupos.models import Grupo
from .forms import ArchivoForm
from .models import Archivo
from .serializers import ArchivoSerializer

User = get_user_model()

# Create your views here.


class ArchivoAPIView(APIView):

    serializer = ArchivoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk=None):
        try:
            grupo = Grupo.objects.get(pk=pk)
            archivos = Archivo.objects.filter(grupo=grupo)
            data = self.serializer(archivos, many=(len(archivos) > 0)).data
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la extraccion de archivos de grupo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, pk=None):
        try:
            archivo_form = ArchivoForm(request.data, request.FILES)
            if archivo_form.is_valid():
                archivo = archivo_form.save(commit=False)
                archivo.creado_por = request.user
                archivo.save()
                return Response({'data': self.serializer(archivo).data}, status=status.HTTP_200_OK)
            return Response({'error': 'Error en la creacion de archivo'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Error en la agregacion de archivo al grupo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk=None):
        try:
            archivo = Archivo.objects.get(pk=pk)
            archivo.activo = False
            archivo.save()
            return Response({'data': 'Archivo desactivado exitosamente'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la desactivacion de archivo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)