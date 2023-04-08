from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarreraSerializer
from .models import Carrera

# Create your views here.


class CarreraAPIView(APIView):

    serializer = CarreraSerializer

    def get(self, request):
        try:
            # Recoger datos
            carreras = Carrera.objects.all()
            # Serializar datos
            data = self.serializer(carreras, many=True).data
            # Respuesta con datos
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Error en la extraccion de las carreas'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
