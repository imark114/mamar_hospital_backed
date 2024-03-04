from rest_framework import serializers
from .models import ContactUs

class ContactUsSerialization(serializers.ModelSerializer):
   class Meta:
    model = ContactUs
    fields = '__all__'
    