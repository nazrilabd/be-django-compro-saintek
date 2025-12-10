from rest_framework import serializers
from .models import HeaderContent

class HeaderContentSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = HeaderContent
        fields = [
            'id', 'title', 'description_short', 'description_full', 'image', 
            'created_by', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']