from django.urls import path
from rest_framework.routers import DefaultRouter

from store import views as st_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from store.views import LogoutView
from users.views import UserProfileView

users_router = DefaultRouter()
users_router.register(r'profiles', UserProfileView, basename='profile')

urlpatterns = [
    path('signup/', st_views.SignupView.as_view(), name='signup'),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
