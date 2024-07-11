from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user


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
        fields = ('first_name', 'last_name', 'email')