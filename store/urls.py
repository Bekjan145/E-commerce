from django.urls import path
from rest_framework.routers import DefaultRouter
from store.views import CartView, CartItemView

from store import views as st_views

store_router = DefaultRouter()
store_router.register(r'category', st_views.CategoryViewSet, basename='category')
store_router.register(r'product', st_views.ProductViewSet, basename='product')

urlpatterns = [
    path("cart/", st_views.CartView.as_view(), name='cart-detail'),
    path("cart/items/", st_views.CartItemView.as_view(), name='cart-items'),
    path('orders/', st_views.OrderListView.as_view(), name='order-list'),
    path('orders/create/', st_views.OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', st_views.OrderDetailView.as_view(), name='order-detail'),
]
