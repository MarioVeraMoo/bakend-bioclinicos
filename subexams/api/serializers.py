from rest_framework import serializers
from subexams.models import SubExam
from exams.api.serializer import ExamSerializer

class SubExamSerializer(serializers.ModelSerializer):
    exam = ExamSerializer()
    
    class Meta:
        model = SubExam
        fields = ['subexam', 'slug' ,'description' ,'exam']
