from rest_framework import serializers
from .models import Post, Tag

# Serializer untuk Model Tag (jika Post memiliki tag)
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

# Serializer untuk Model Post
class PostSerializer(serializers.ModelSerializer):
    # Mengubah relasi Foreign Key ke username agar lebih informatif
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    
    # Mengubah relasi Many-to-Many ke representasi TagSerializer
    tags = TagSerializer(many=True, read_only=True) 

    class Meta:
        model = Post
        # Tentukan field mana saja yang ingin Anda tampilkan di API
        fields = (
            'id', 'title', 'slug', 'description', 'image', 
            'created_by', 'tags', 'created_at', 'updated_at'
        )
        # Jika Anda ingin menampilkan SEMUA field: fields = '__all__'