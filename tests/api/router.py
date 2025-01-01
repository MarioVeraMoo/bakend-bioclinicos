from rest_framework.routers import DefaultRouter
from tests.api.views import TestsApiViewSet

router_tests= DefaultRouter()

router_tests.register(prefix='tests', basename='tests', viewset=TestsApiViewSet)