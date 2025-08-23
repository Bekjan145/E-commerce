from rest_framework.viewsets import ModelViewSet
from store.models import Product, Category
from store.serializers import ProductSerializer, CategorySerializer


# Create your views here.


# Category CRUD
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Product CRUD
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
