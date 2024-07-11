from django.core.cache import cache

import random
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from jwt.utils import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import RegisterSerializer, ConfirmSerializer, PasswordResetSerializer, \
    PasswordResetLoginSerializer, UserSerializer
from .models import User
from .tasks import send_email


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def generic_confirmation_code(self):
        return random.randrange(100000, 900000)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        first_name = serializer.validated_data['first_name']
        last_name = serializer.validated_data['last_name']
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        confirm_password = serializer.validated_data['confirm_password']

        confirmation_code = self.generic_confirmation_code()

        cache_data = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'password': password,
            'confirmation_code': confirmation_code
        }

        cache.set(email, cache_data, timeout=300)
        send_email.delay(email, confirmation_code)
        return Response({'confirm_code': confirmation_code}, status=status.HTTP_201_CREATED)


class ConfirmationCodeAPIView(GenericAPIView):
    serializer_class = ConfirmSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        confirm_code = request.data.get('confirm_code')
        cashed_data = cache.get(email)

        if cashed_data and confirm_code == cashed_data.get('confirmation_code'):
            first_name = cashed_data.get('first_name')
            last_name = cashed_data.get('last_name')
            username = cashed_data.get('username')
            password = cashed_data.get('password')

            if User.objects.filter(email=email).exists():
                return Response({'success': False, 'message': 'This email already exists!'},
                                status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(username=username).exists():
                return Response({'success': False, 'message': 'This username already exists!'})
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password
                )
                return Response({'success': True})
        else:
            return Response({'message': 'The entered code is not valid!'}, status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestView(GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

            uid = urlsafe_base64_encode(force_bytes(str(user.pk)))
            token = default_token_generator.make_token(user)
            resent_link = f"http://127.0.0.1:8000/accounts/reset-password/reset/{uid}/{token}"


class PasswordResetView(GenericAPIView):
    serializer_class = PasswordResetLoginSerializer

    def post(self, request, uid, token):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            new_password = serializer.validated_data['new_password']

            try:
                uid = force_str(urlsafe_base64_decode(uid))
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None
            if user is not None and default_token_generator.check_token(user, token):
                user.set_password(new_password)
                user.save()
                return Response({'success': 'Password reset successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)