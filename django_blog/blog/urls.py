from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from blog.views import PostListView, CommentCreateView, CommentUpdateView, CommentDeleteView,  PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('comment<int:pk>/update/', CommentUpdateView.as_view(), name = 'update-comment'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name = "post-comment"),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment')

]


