from django.urls import path
from .views import PostListAPIView

urlpatterns = [
    # URL: /api/posts/ atau /api/blog/
    path('', PostListAPIView.as_view(), name='post-list-api'),
]