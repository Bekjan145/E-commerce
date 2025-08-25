from django.urls import path

from users import views as us_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', us_views.SignupView.as_view(), name='signup'),
    path("profile/", us_views.UserProfileView.as_view(), name="user-profile"),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api/logout/', us_views.LogoutView.as_view(), name='logout'),
]
