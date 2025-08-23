from django.contrib import admin

from store.models import Product, Category, Cart, CartItem

admin.site.register((Product, Category, Cart, CartItem))
