from django.urls import path
from .views import UserRegistrationView,LogoutView
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
    
]