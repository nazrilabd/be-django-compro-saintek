from django.urls import path
from .views import PostListAPIView, PostDetailAPIView,TagListAPIView # Import View yang baru

urlpatterns = [
    # 1. URL List (GET semua postingan)
    path('', PostListAPIView.as_view(), name='post-list-api'),
    
    # 2. URL Detail (GET satu postingan berdasarkan ID)
    # <int:pk> menunjukkan bahwa bagian ini adalah Primary Key (ID) dan harus berupa integer
    path('<int:pk>/', PostDetailAPIView.as_view(), name='post-detail-api'), 
    path('tags/', TagListAPIView.as_view(), name='tag-list-api'),

]