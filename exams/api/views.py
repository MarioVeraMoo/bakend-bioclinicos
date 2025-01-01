from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from exams.models import Exam
from exams.api.serializer import ExamSerializer
#from doctor.api.permissions import IsAdminOrReadOnly

class ExamsApiViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__slug']