from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    # Mengubah relasi Foreign Key ke username agar lebih informatif
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Announcement
        fields = [
            'id', 
            'title', 
            'description', 
            'created_by', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']