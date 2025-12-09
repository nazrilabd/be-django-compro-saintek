from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# View untuk mengambil daftar semua Postingan
class PostListAPIView(generics.ListAPIView):
    # Tentukan Queryset: Data apa yang ingin diambil?
    queryset = Post.objects.all()
    
    # Tentukan Serializer: Bagaimana data tersebut harus diformat?
    serializer_class = PostSerializer