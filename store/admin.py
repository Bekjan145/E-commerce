from django.contrib import admin

from store.models import Product, Category, Cart, CartItem, Order, OrderItem

admin.site.register((Product, Category, Cart, CartItem, Order, OrderItem))
