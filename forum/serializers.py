from rest_framework import serializers
from .models import ForumPost, Tag

# Asumsi: TagSerializer sudah ada atau dibuat di sini
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class ForumPostSerializer(serializers.ModelSerializer):
    # Untuk GET response: tampilkan username
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    # Field untuk menerima ID Tag saat POST/PUT
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), 
        source='tags', 
        many=True, 
        write_only=True,
        required=False
    )
    
    class Meta:
        model = ForumPost
        fields = [
            'id', 'title', 'description', 
            'created_by', 'created_at', 'tags', 
            'tag_ids' # Hanya digunakan saat input (write_only)
        ]
        read_only_fields = ['created_at']