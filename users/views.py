from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from users.serializers import UserProfileSerializers


class UserProfileView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializers
