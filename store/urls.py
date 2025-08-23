from django.urls import path
from rest_framework.routers import DefaultRouter
from store.views import CartView, CartItemView

from store import views as st_views

store_router = DefaultRouter()
store_router.register(r'category', st_views.CategoryViewSet, basename='category')
store_router.register(r'product', st_views.ProductViewSet, basename='product')

urlpatterns = [
    path("cart/", CartView.as_view(), name='cart-detail'),
    path("cart/items/", CartItemView.as_view(), name='cart-items')
]
