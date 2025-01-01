from rest_framework import serializers
from exams.models import Exam
from categories.api.serializers import CategorySerializer

class ExamSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Exam
        fields = ['exam', 'slug' ,'titleExam','price','discount', 'description' ,'indications','miniature','category']
