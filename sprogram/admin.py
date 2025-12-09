# akademik/admin.py
from django.contrib import admin
from .models import ProgramStudi

@admin.register(ProgramStudi)
class ProgramStudiAdmin(admin.ModelAdmin):
    # Field yang akan ditampilkan di halaman daftar
    list_display = (
        'name_programstudy', 
        'kaprodi_name', 
        'name_hima'
    )
    # Membuat field mudah dicari
    search_fields = (
        'name_programstudy', 
        'kaprodi_name'
    )