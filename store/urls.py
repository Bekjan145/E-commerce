from django.urls import path
from store import views as st_views

urlpatterns = [
    path('signup/', st_views.SignupView.as_view(), name='signup'),
]
