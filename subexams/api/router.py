from rest_framework.routers import DefaultRouter
from subexams.api.views import SubExamsApiViewSet

router_subexams = DefaultRouter()

router_subexams.register(prefix='subexams', basename='subexams', viewset=SubExamsApiViewSet)