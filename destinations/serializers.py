from rest_framework import serializers
from .models import Destination

class DestinationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    description = serializers.CharField(required=True,style={'base_template': 'textarea'})
    best_time_to_visit = serializers.CharField(required=True)
    category = serializers.CharField(required=True)
    image_url = serializers.URLField(required=True)
    class Meta:
        model = Destination
        fields = '__all__'
