from rest_framework.routers import DefaultRouter
from doctor.api.views import DoctorsApiViewSet

router_doctors = DefaultRouter()

router_doctors.register(prefix='doctors', basename='doctors', viewset=DoctorsApiViewSet)