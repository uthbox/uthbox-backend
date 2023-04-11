from django.urls import path
from .views import PerfilAPIView, PerfilesFiltroAPIView, PerfilesAPIView, RelacionesAPIView

# Define your urls here.

urlpatterns = [
    path('personal', PerfilAPIView.as_view(), name='perfil'),
    path('filtro', PerfilesFiltroAPIView.as_view(), name='filtrar_perfil'),
    path('lista', PerfilesAPIView.as_view(), name='lista_perfiles'),
    path('<int:pk>', PerfilesAPIView.as_view(), name='perfil_usuario'),
    path('seguir', RelacionesAPIView.as_view(), name='seguir_perfil'),
    path('seguir/<int:pk>', RelacionesAPIView.as_view(), name='seguir_perfil'),
]
