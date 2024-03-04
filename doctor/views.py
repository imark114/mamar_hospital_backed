from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Specialization, Designation, AvilableTime, Doctor, Review
from .serialization import SpecializationSerialization, DesignationSerialization, AvilableTimeSerialization, DoctorSerialization, ReviewSerialization
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class= SpecializationSerialization

class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class= DesignationSerialization

class AvilabletimeSpecificDoc(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return query_set.filter(doctor=doctor_id)
        return query_set

class AvilableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AvilableTime.objects.all()
    serializer_class= AvilableTimeSerialization
    filter_backends = [AvilabletimeSpecificDoc]

class DoctorPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 100

class DcotorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class= DoctorSerialization
    pagination_class = DoctorPagination
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class= ReviewSerialization




