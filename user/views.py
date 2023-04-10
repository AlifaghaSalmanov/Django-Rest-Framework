from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from .serializer import LoginSerializer, RegisterSerializer


@api_view(["POST"])
def LoginView(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    else:
        return Response(
            {"detail": "username or password is incorrect"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    class Meta:
        model = User
        fields = ("username", "password")


# Create your views here.
