from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
#from doctor.api.permissions import IsAdminOrReadOnly

class CategoriesApiViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'
