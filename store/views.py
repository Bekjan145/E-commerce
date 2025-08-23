from rest_framework.viewsets import ModelViewSet
from store.models import Product, Category, Cart, CartItem
from rest_framework import generics
from store.serializers import ProductSerializer, CategorySerializer, CartSerializer, CartItemSerializers


# Create your views here.


# Category CRUD
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Product CRUD
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartView(generics.RetrieveDestroyAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


class CartItemView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = CartItemSerializers

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)
