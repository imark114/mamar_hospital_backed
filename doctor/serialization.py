from rest_framework import serializers
from .models import Specialization,Designation,AvilableTime,Doctor,Review

class SpecializationSerialization(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class DesignationSerialization(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class AvilableTimeSerialization(serializers.ModelSerializer):
    class Meta:
        model = AvilableTime
        fields = '__all__'

class DoctorSerialization(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True)
    specialization = serializers.StringRelatedField(many=True)
    avilable_time = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'

class ReviewSerialization(serializers.ModelSerializer):
    reviewr = serializers.StringRelatedField(many=False)
    doctor = serializers.StringRelatedField(many=False)

    class Meta:
        model = Review
        fields = '__all__'
