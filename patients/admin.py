from django.contrib import admin
from patients.models import Patients

# Register your models here.
@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'first_surname','second_surname','address','phone_number']