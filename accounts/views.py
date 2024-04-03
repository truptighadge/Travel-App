from django.shortcuts import render
from rest_framework import generics
from .serializers import UserRegistrationSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  
        if serializer.is_valid(): 
            serializer.save()
            return Response({"message": "Registration successfully."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class LogoutView(APIView):
    def post(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split()[1]
            token_obj = Token.objects.get(key=token)
            token_obj.delete()
            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

