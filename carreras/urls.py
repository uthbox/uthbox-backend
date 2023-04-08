from django.urls import path
from .views import CarreraAPIView

# Define your urls here.

urlpatterns = [
    path('', CarreraAPIView.as_view(), name='carreras')
]