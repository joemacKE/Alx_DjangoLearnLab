from django.urls import path
from .views import RegisterAPIView, LogOutAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('accounts/register/', RegisterAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('accounts/logout/', LogOutAPIView.as_view(), name='logout')
]