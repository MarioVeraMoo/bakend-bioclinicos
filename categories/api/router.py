from rest_framework.routers import DefaultRouter
from categories.api.views import CategoriesApiViewSet

router_categories = DefaultRouter()

router_categories.register(prefix='categories', basename='categories', viewset=CategoriesApiViewSet)