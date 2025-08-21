from django.urls import path
from rest_framework.routers import DefaultRouter

from store import views as st_views

router = DefaultRouter()
router.register(r'category', st_views.CategoryViewSet, basename='category')
router.register(r'product', st_views.ProductViewSet, basename='product')

urlpatterns = [
    path('signup/', st_views.SignupView.as_view(), name='signup'),
]
