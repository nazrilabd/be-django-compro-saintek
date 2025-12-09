from rest_framework import viewsets, permissions
from .models import ForumPost
from .serializers import ForumPostSerializer

# Custom Permission: Hanya pembuat yang bisa edit/hapus
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS diizinkan untuk siapa saja
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # WRITE permissions (POST, PUT, DELETE) hanya untuk pemilik postingan
        return obj.created_by == request.user

# ViewSet untuk menangani semua operasi CRUD
class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    
    # Set permissions: IsAuthenticatedOrReadOnly (siapa saja bisa GET, harus login untuk POST)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # --- Override perform_create untuk mengisi created_by secara otomatis ---
    def perform_create(self, serializer):
        # Mengisi field created_by dengan user yang sedang login
        serializer.save(created_by=self.request.user)