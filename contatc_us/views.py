from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUs
from .serializations import ContactUsSerialization

# Create your views here.

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerialization
