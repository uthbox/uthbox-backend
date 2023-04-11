from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notificaciones.models import Notificacion
from .models import Grupo
from .forms import GrupoForm
from .serializers import GrupoSerializer

User = get_user_model()

# Create your views here.


class GrupoAPIView(APIView):

    serializer = GrupoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk=None):
        try:
            if pk is not None:
                grupo = Grupo.objects.get(pk=pk, creado_por=request.user, activo=True)
                data = self.serializer(grupo).data
            else:
                grupos = Grupo.objects.filter(creado_por=request.user, activo=True)
                data = self.serializer(grupos, many=True).data
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la extraccion de grupos'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        # Recolectar datos
        grupo_form = GrupoForm(request.data)
        # Validar Datos
        if grupo_form.is_valid():
            grupo = grupo_form.save(commit=False)
            grupo.creado_por = request.user
            grupo.save()
            grupo.usuarios.add(request.user)
            data = self.serializer(grupo).data
            # Respuesta de API
            return Response({'data': data}, status=status.HTTP_200_OK)
        # Error de Request
        return Response({'error': grupo_form.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            # Recolectar datos
            grupo_actual = Grupo.objects.get(pk=pk)
            grupo_form = GrupoForm(request.data, instance=grupo_actual)
            # Validar Datos
            if grupo_form.is_valid():
                grupo = grupo_form.save()
                data = self.serializer(grupo).data
                # Respuesta de API
                return Response({'data': data}, status=status.HTTP_200_OK)
            # Error de Request
            return Response({'error': grupo_form.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Error en la actualizacion de grupo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk=None):
        try:
            grupo = Grupo.objects.get(pk=pk)
            grupo.activo = False
            grupo.save()
            data = self.serializer(grupo).data
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la desactivacion de grupo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GruposListaAPIView(APIView):

    serializer = GrupoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        try:
            grupos = Grupo.objects.filter(usuarios__in=[request.user])
            data = self.serializer(grupos, many=True).data
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la extraccion de grupos'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AgregarIntegranteAPIView(APIView):

    serializer = GrupoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def patch(self, request, pk=None):
        try:
            integrantes = request.data.get('integrantes')
            usuario = User.objects.get(pk=integrantes[0])
            grupo = Grupo.objects.get(pk=pk, activo=True)
            grupo.usuarios.add(usuario)
            Notificacion.objects.create(titulo=grupo.nombre, mensaje='{} {} te ha agregado al grupo de {}'.format(request.user.first_name, request.user.last_name, grupo.nombre), usuario=usuario, usuario_creador=request.user)
            data = self.serializer(grupo).data
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la agregacion de integrante al grupo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



