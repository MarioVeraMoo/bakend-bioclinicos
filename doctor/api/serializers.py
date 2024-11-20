from rest_framework import serializers
from doctor.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'midle_name' ,'first_surname','second_surname','phone_number','email']