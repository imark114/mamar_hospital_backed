from django.db import models
from doctor.models import Doctor, AvilableTime
from patient.models import Patient
# Create your models here.
APPOINTMENT_TYPES=[
    ('Offline', 'Offline'),
    ('Online', 'Online')
]

APPOINTMENT_STATUS=[
    ('Pending', 'Pending'),
    ('Running', 'Running'),
    ('Completed', 'Completed'),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_types = models.CharField(max_length=10,choices=APPOINTMENT_TYPES)
    appointment_status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS, default='Pending')
    symptom = models.TextField()
    time = models.ForeignKey(AvilableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name}, Patient: {self.patient.user.first_name}"
    