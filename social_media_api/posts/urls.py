from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostListViewSet, CommentListViewSet

router = DefaultRouter()
router.register(r'posts', PostListViewSet, basename='posts')
router.register(r'comments', CommentListViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls))
]