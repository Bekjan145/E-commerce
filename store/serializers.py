from rest_framework import serializers
from store.models import Product, Category


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


