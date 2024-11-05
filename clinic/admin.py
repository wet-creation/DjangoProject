from django.contrib import admin
from .models import Doctor, Patient, Stay

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'first_name', 'last_name', 'specialization', 'experience_years')
    search_fields = ('first_name', 'last_name', 'specialization')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'first_name', 'last_name', 'category', 'birth_year')
    search_fields = ('first_name', 'last_name', 'phone_number')

class StayAdmin(admin.ModelAdmin):
    list_display = ('stay_id', 'get_patient_first_name', 'get_doctor_first_name')

    def get_patient_first_name(self, obj):
        return obj.patient.first_name if obj.patient else 'N/A'
    get_patient_first_name.short_description = 'Patient First Name'

    def get_doctor_first_name(self, obj):
        return obj.doctor.first_name if obj.doctor else 'N/A'
    get_doctor_first_name.short_description = 'Doctor First Name'

    list_filter = ('doctor', 'patient')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Stay, StayAdmin)
