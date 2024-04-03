from django.shortcuts import render
from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status




class DestinationListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class DestinationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Record deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

