from rest_framework.routers import DefaultRouter
from patients.api.views import PatientsApiViewSet

router_patients = DefaultRouter()

router_patients.register(prefix='patients', basename='patients', viewset=PatientsApiViewSet)