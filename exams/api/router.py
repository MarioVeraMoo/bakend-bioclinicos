from rest_framework.routers import DefaultRouter
from exams.api.views import ExamsApiViewSet

router_exams = DefaultRouter()

router_exams.register(prefix='exams', basename='exams', viewset=ExamsApiViewSet)