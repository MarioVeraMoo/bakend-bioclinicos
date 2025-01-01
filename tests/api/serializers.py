from rest_framework import serializers
from tests.models import Tests
#from exams.api.serializer import ExamSerializer

class TestSerializer(serializers.ModelSerializer):
    #exam = ExamSerializer()
    
    class Meta:
        model = Tests
        fields = ['test', 'slug' ,'unitofmeasurement','method','description' ,'subexam']


