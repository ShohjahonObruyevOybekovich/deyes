from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import User


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class ConfirmSerializer(Serializer):
    email = serializers.EmailField()
    confirm_code = serializers.IntegerField()


class PasswordResetSerializer(Serializer):
    email = serializers.EmailField()


class PasswordResetLoginSerializer(Serializer):
    new_password = serializers.CharField()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
