from django.urls import path
from .views import AnnouncementListAPIView, AnnouncementDetailAPIView

urlpatterns = [
    # 1. URL List (GET semua pengumuman, mendukung search, pagination)
    # URL: /api/pengumuman/
    path('', AnnouncementListAPIView.as_view(), name='announcement-list-api'),
    
    # 2. URL Detail (GET satu pengumuman berdasarkan ID)
    # URL: /api/pengumuman/5/
    path('<int:pk>/', AnnouncementDetailAPIView.as_view(), name='announcement-detail-api'), 
]