from django.urls import path
from .views import MensajeAPIView

# Define your urls here.

urlpatterns = [
    path('<int:pk>', MensajeAPIView.as_view(), name='grupos'),
]