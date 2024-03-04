from django.contrib import admin
from .models import Patient
# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone']

    def first_name(self, obj):
       return obj.user.first_name
