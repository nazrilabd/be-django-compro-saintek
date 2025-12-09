from rest_framework import generics
from .models import ProgramStudi
from .serializers import ProgramStudiSerializer

# View untuk mengambil daftar semua Program Studi
class ProgramStudiListAPIView(generics.ListAPIView):
    # Queryset: ambil semua objek ProgramStudi
    queryset = ProgramStudi.objects.all()
    
    # Serializer: gunakan serializer yang baru kita buat
    serializer_class = ProgramStudiSerializer