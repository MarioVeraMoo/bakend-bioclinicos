from rest_framework.viewsets import ModelViewSet
from patients.models import Patients
from patients.api.serializers import PatientSerializer
from patients.api.permissions import IsAdminOrReadOnly

class PatientsApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PatientSerializer
    queryset = Patients.objects.all()