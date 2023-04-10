from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")


class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ("token",)

    def get_token(self, instance):
        token_tuple = Token.objects.get_or_create(user=instance)
        token = token_tuple[0]
        return token.key
