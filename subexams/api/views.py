from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from subexams.models import SubExam
from subexams.api.serializers import SubExamSerializer
#from doctor.api.permissions import IsAdminOrReadOnly

class SubExamsApiViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = SubExamSerializer
    queryset = SubExam.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['exam__slug']