from rest_framework import generics, filters
from .models import HeaderContent
from .serializers import HeaderContentSerializer

class HeaderContentListAPIView(generics.ListAPIView):
    queryset = HeaderContent.objects.all()
    serializer_class = HeaderContentSerializer
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # Perbarui search_fields agar mencakup kedua deskripsi
    search_fields = ['title', 'description_short', 'description_full'] 
    ordering_fields = ['created_at', 'title'] 

class HeaderContentDetailAPIView(generics.RetrieveAPIView):
    queryset = HeaderContent.objects.all()
    serializer_class = HeaderContentSerializer