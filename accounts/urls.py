from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import RegisterView, ConfirmationCodeAPIView, PasswordResetRequestView, PasswordResetView, UserInfo

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm-code/', ConfirmationCodeAPIView.as_view(), name='confirm_code'),
    path('forget-password', PasswordResetRequestView.as_view(), name='forget_password'),
    path('reset-password/<str:uid>/<str:token>', PasswordResetView.as_view(), name='reset_password'),
    path('user-info/', UserInfo.as_view(), name='user_info'),
]
