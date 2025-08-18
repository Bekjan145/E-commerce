from rest_framework import generics, viewsets

from store.models import Product, Category
from store.serializer import ProductSerializer, CategorySerializer, SignupSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


# Create your views here.


# Category CRUD
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Product CRUD
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        operation_description="Выйти из системы (инвалидировать refresh токен)",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Refresh токен, который нужно сделать недействительным"
                )
            },
            required=['refresh']
        ),
        responses={
            200: openapi.Response(description="Успешный выход"),
            400: openapi.Response(description="Невалидный токен")
        }
    )
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response("Успешный выход")
        except Exception as e:
            return Response({'error': "Невалидный токен"}, status=status.HTTP_400_BAD_REQUEST)


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
