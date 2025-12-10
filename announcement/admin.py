from django.contrib import admin
from .models import Announcement

# --- DAFTAR KE ADMIN PANEL ---
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    # Field yang akan ditampilkan di halaman daftar Pengumuman
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    
    # Field yang dapat digunakan untuk filter cepat di sidebar
    list_filter = ('created_at', 'updated_at')
    
    # Field yang dapat dicari
    search_fields = ('title', 'description')
    
    # Mengatur field mana yang hanya bisa dibaca (read-only)
    readonly_fields = ('created_at', 'updated_at')
    
    # Mengatur tampilan form (fieldsets)
    fieldsets = (
        ('📝 Informasi Pengumuman', {
            # created_by dihilangkan dari tampilan form agar terisi otomatis di save_model
            'fields': ('title', 'description'), 
        }),
        ('⏰ Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',), # Opsional: membuat bagian ini tertutup secara default
        }),
    )

    # --- Override save_model untuk mengisi created_by secara otomatis ---
    # Ini adalah langkah KRUSIAL agar created_by terisi otomatis
    def save_model(self, request, obj, form, change):
        # Jika objek baru dibuat (obj.pk belum ada)
        if not obj.pk:
            # Isi created_by dengan user yang sedang login saat ini
            obj.created_by = request.user
        
        super().save_model(request, obj, form, change)