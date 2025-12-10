from django.contrib import admin
from .models import HeaderContent

@admin.register(HeaderContent)
class HeaderContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    
    # Search sekarang mencakup kedua field deskripsi
    search_fields = ('title', 'description_short', 'description_full') 
    
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Konten Utama', {
            # Tambahkan kedua field deskripsi di sini
            'fields': ('title', 'description_short', 'description_full', 'image'), 
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)