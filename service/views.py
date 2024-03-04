from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from .serialization import ServiceSerialization

# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerialization