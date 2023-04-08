from django.urls import path
from .views import GrupoAPIView, GruposListaAPIView, AgregarIntegranteAPIView

# Define your urls here.

urlpatterns = [
    path('', GrupoAPIView.as_view(), name='grupos'),
    path('<int:pk>', GrupoAPIView.as_view(), name='grupo'),
    path('<int:pk>/agregar', AgregarIntegranteAPIView.as_view(), name='grupo_detalle'),
    path('lista', GruposListaAPIView.as_view(), name='grupos_lista'),
]