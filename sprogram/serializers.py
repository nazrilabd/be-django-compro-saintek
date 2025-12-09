from rest_framework import serializers
from .models import ProgramStudi

class ProgramStudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramStudi
        # Tentukan field yang akan ditampilkan di API
        fields = (
            'id', 
            'name_programstudy', 
            'about_programstudy', 
            'cover_header', 
            'name_hima', 
            'cover_hima', 
            'description_hima', 
            'kaprodi_profile', 
            'kaprodi_name', 
            'kaprodi_description'
        )