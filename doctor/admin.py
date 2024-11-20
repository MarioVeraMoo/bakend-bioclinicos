from django.contrib import admin
from doctor.models import Doctor
# Register your models here.
@admin.register(Doctor)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'first_surname','second_surname','phone_number','email']