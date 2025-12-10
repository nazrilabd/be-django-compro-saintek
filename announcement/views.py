from rest_framework import generics, filters
from .models import Announcement
from .serializers import AnnouncementSerializer

# --- VIEW UNTUK LIST (GET semua pengumuman) ---
class AnnouncementListAPIView(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    
    # Backends untuk Search, Pagination (dari settings), dan Sorting
    filter_backends = [
        filters.SearchFilter, 
        filters.OrderingFilter 
    ]

    # Mencari kata kunci di field 'title' dan 'description'
    search_fields = ['title', 'description']

    # Mengizinkan sorting berdasarkan created_at atau title
    ordering_fields = ['created_at', 'title'] 

# --- VIEW UNTUK DETAIL (GET berdasarkan ID) ---
class AnnouncementDetailAPIView(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    # lookup_field default-nya adalah 'pk' (ID)