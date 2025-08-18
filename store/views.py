from django.contrib.auth.models import User
from rest_framework import generics
from .serializer import SignupSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
