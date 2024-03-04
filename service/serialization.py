from rest_framework import serializers
from .models import Service

class ServiceSerialization(serializers.ModelSerializer):
   class Meta:
    model = Service
    fields = '__all__'
    