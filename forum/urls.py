
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from forum.views import ForumPostViewSet # Import ViewSet

# 1. Inisialisasi Router
router = DefaultRouter()

# 2. Daftarkan ViewSet Anda (otomatis membuat 5 endpoint)
# Endpoint utama akan menjadi /api/forum/
router.register(r'', ForumPostViewSet, basename='forum')

urlpatterns = [
  
    # 3. Masukkan URL Router
    path('', include(router.urls)), # <-- Semua URL CRUD ada di sini
]