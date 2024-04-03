from django.urls import path
from .views import DestinationListCreateAPIView, DestinationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', DestinationListCreateAPIView.as_view(), name='destination-list-create'),
    path('<int:pk>/', DestinationRetrieveUpdateDestroyAPIView.as_view(), name='destination-detail'),
]

