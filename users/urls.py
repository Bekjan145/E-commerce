from django.urls import path
from rest_framework.routers import DefaultRouter

from store import views as st_views
from users import views as us_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserProfileView

users_router = DefaultRouter()
users_router.register(r'profiles', UserProfileView, basename='profile')

urlpatterns = [
    path('signup/', us_views.SignupView.as_view(), name='signup'),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api/logout/', us_views.LogoutView.as_view(), name='logout'),
]
