from rest_framework.viewsets import ModelViewSet
from doctor.models import Doctor
from doctor.api.serializers import DoctorSerializer
from doctor.api.permissions import IsAdminOrReadOnly

class DoctorsApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
