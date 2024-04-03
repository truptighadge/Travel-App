from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Destination

class DestinationAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Test Time',
            category='Beach',
            image_url='http://example.com/test_image.jpg'
        )


    def test_destination_list(self):
        url = reverse('destination-list-create')
        # Authenticate the user before making the request
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)    
    
    def test_destination_detail(self):
        url = reverse('destination-detail', kwargs={'pk': self.destination.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Checking if unauthorized without authentication
        # Now, authenticate the user and make the request again
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Destination')

    
    def test_destination_creation(self):
        url = reverse('destination-list-create')
        data = {
            'name': 'New Destination',
            'country': 'New Country',
            'description': 'New Description',
            'best_time_to_visit': 'New Time',
            'category': 'Mountain',
            'image_url': 'http://example.com/new_image.jpg'
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Destination.objects.count(), 2)
    
    def test_destination_update(self):
        url = reverse('destination-detail', kwargs={'pk': self.destination.pk})
        data = {
            'name': 'Updated Destination',
            'country': 'Updated Country',
            'description': 'Updated Description',
            'best_time_to_visit': 'Updated Time',
            'category': 'City',
            'image_url': 'http://example.com/updated_image.jpg'
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.destination.refresh_from_db()
        self.assertEqual(self.destination.name, 'Updated Destination')
        self.assertEqual(self.destination.country, 'Updated Country')
       
    
    def test_destination_delete(self):
        url = reverse('destination-detail', kwargs={'pk': self.destination.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Destination.objects.count(), 0)
    
    def test_authentication_required(self):
        url = reverse('destination-list-create')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_invalid_data_error_handling(self):
        url = reverse('destination-list-create')
        data = {}  # Invalid data
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
