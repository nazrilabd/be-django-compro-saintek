# blog/admin.py

from django.contrib import admin
from .models import Post, Tag # Impor model yang sudah dibuat

# Daftarkan Model Tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # Field yang akan ditampilkan di halaman daftar Tag
    list_display = ('name', 'slug')
    # Membuat field slug terisi otomatis dari name saat mengisi form
    prepopulated_fields = {'slug': ('name',)}


# Daftarkan Model Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Field yang ditampilkan di halaman daftar Postingan
    list_display = ('title', 'created_at', 'updated_at','created_by')
    
    # Field yang bisa digunakan untuk filter
    list_filter = ('created_at', 'updated_at', 'tags')
    
    # Field yang bisa dicari
    search_fields = ('title', 'description')
    
    # Membuat field slug terisi otomatis dari title saat mengisi form
    prepopulated_fields = {'slug': ('title',)}
    
    # Menyertakan ManyToManyField (tags) di form admin
    filter_horizontal = ('tags',) 
    
    # Mengatur tampilan form
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'created_by', 'image', 'description', 'tags')
        }),
    )