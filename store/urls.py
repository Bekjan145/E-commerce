from django.urls import path

from store import views as st_views

urlpatterns = [
    path('category/', st_views.CategoryListCreateView.as_view()),
    path('category/<int:pk>/', st_views.CategoryRUDView.as_view()),
    path('product/', st_views.ProductListCreateView.as_view()),
    path('product/<int:pk>', st_views.ProductRUDView.as_view()),
]
