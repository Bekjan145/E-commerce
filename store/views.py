from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializer import SignupSerializer

User = get_user_model()


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
