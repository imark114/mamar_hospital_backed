from django.contrib import admin
from .models import Specialization, Designation, AvilableTime,Doctor,Review
# Register your models here.
@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug': ('name',),}

admin.site.register(AvilableTime)
admin.site.register(Doctor)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['reviwer_name', 'doctor_name']

    def reviwer_name(self,obj):
       return obj.reviewr.user.first_name
    def doctor_name(self,obj):
       return obj.doctor.user.first_name
