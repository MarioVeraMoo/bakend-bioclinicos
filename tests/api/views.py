from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from tests.models import Tests
from tests.api.serializers import TestSerializer
#from doctor.api.permissions import IsAdminOrReadOnly

class TestsApiViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = TestSerializer
    queryset = Tests.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subexam__slug']