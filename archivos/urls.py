from django.urls import path
from .views import ArchivoAPIView

# Define your urls here.

urlpatterns = [
    path('<int:pk>', ArchivoAPIView.as_view(), name='Archivo')
]