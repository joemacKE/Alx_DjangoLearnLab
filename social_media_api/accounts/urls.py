from django.urls import path
from .views import RegisterAPIView, LogOutAPIView, FollowersListAPIView, UnfollowAUserPIView, FollowingListAPIView, FollowUserAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('accounts/register/', RegisterAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('accounts/logout/', LogOutAPIView.as_view(), name='logout'),
    path('<int:user_id>/follow/', FollowUserAPIView.as_view(), name='follow-user'),
    path('<int:user_id>/unfollow/', UnfollowAUserPIView.as_view(), name='unfollow-user'),
    path('<int:user_id>/followers/', FollowersListAPIView.as_view(), name='followers-list'),
    path('<int:user_id>/following/', FollowingListAPIView.as_view(), name='following-list'),
]