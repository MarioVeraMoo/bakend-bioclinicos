from rest_framework import serializers
from patients.models import Patients

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['first_name', 'midle_name' ,'first_surname','second_surname','birthdate','gender','address','phone_number','email']