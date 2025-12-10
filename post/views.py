from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend 
from .models import Post,Tag
from .serializers import PostSerializer,TagSerializer
class TagListAPIView(generics.ListAPIView):
    # Queryset: Ambil semua objek Tag
    queryset = Tag.objects.all()
    
    # Serializer: Gunakan TagSerializer
    serializer_class = TagSerializer
    
    # Opsional: Agar tag diurutkan berdasarkan nama
    ordering_fields = ['name']
# View untuk mengambil daftar semua Postingan (List View, sudah ada sebelumnya)
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    filterset_fields = ['tags__name'] 
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'updated_at', 'title'] 

# --- VIEW BARU UNTUK DETAIL BERDASARKAN ID ---
class PostDetailAPIView(generics.RetrieveAPIView):
    # Tentukan Queryset: Data apa yang ingin diambil?
    queryset = Post.objects.all()
    
    # Tentukan Serializer: Bagaimana data tersebut harus diformat?
    serializer_class = PostSerializer
    
    # lookup_field default-nya adalah 'pk' (Primary Key/ID), 
    # jadi Anda tidak perlu menentukannya lagi kecuali ingin menggunakan slug
    # lookup_field = 'pk'