# forum/admin.py
from django.contrib import admin
from .models import ForumPost, Comment, Vote, Tag # Impor Tag

# Mendaftarkan Model Tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


# Mendaftarkan Model Postingan
@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'total_likes', 'total_dislikes')
    search_fields = ('title', 'description', 'created_by__username')
    readonly_fields = ('created_at',)
    
    # Tambahkan filter_horizontal agar tampilan Many-to-Many (Tags) lebih bagus
    filter_horizontal = ('tags',) 

    # Fieldsets yang sudah diperbarui
    fieldsets = (
        ('📝 Informasi Utama', {
            'fields': ('title', 'description', 'tags') # Tags ada di sini
        }),
        ('👤 Informasi Penulis & Waktu', {
            'fields': ('created_by', 'created_at'),
        }),
    )


# Mendaftarkan Model Komentar
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'commented_by', 'created_at')
    search_fields = ('content', 'commented_by__username')
    readonly_fields = ('created_at',)

# Mendaftarkan Model Vote
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'vote_type')
    list_filter = ('vote_type',)