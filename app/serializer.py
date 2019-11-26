from app.models import Welcome
from rest_framework import serializers

class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welcome
        fields = '__all__'

