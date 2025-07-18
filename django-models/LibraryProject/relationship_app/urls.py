from .views import views
from django.urls import path

urlpatterns = [
    path('books/', views.BookViews.as_view(), name='books' )
]