from rest_framework import serializers
from store.models import Product, Category, Cart, CartItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'stock', 'category', 'created_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
        }


class CartItemSerializers(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = CartItem
        fields = ["id", "product", "product_name", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializers(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "items", "created_at"]
        read_only_fields = ["user"]
