from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Pilihan untuk status Vote (Like atau Dislike)
VOTE_CHOICES = (
    (1, 'Like'),
    (-1, 'Dislike'),
)

# ==============================================================================
# 1. Model Tag (Daftar Tag untuk Forum)
# ==============================================================================
class Tag(models.Model):
    # Nama tag, harus unik (misalnya: 'python', 'database', 'frontend')
    name = models.CharField(max_length=50, unique=True)
    # Slug untuk URL yang rapi
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Otomatis membuat slug dari nama jika belum ada
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Tags Forum"
        ordering = ['name']

    def __str__(self):
        return self.name

# ==============================================================================
# 2. Model ForumPost (Postingan Utama) - DITAMBAH TAGS
# ==============================================================================
class ForumPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Judul Postingan")
    description = models.TextField(verbose_name="Isi Postingan")
    
    # --- FIELD BARU: Tags ---
    # Relasi Many-to-Many ke Model Tag
    tags = models.ManyToManyField(Tag, blank=True) 

    created_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='forum_posts',
        verbose_name="Dibuat Oleh"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Postingan Forum"
        verbose_name_plural = "Postingan Forum"
        ordering = ['-created_at'] 
        
    def __str__(self):
        return self.title
        
    def total_likes(self):
        return self.votes.filter(vote_type=1).count()

    def total_dislikes(self):
        return self.votes.filter(vote_type=-1).count()


# ==============================================================================
# 3. Model Comment (Komentar) - TIDAK BERUBAH
# ==============================================================================
class Comment(models.Model):
    post = models.ForeignKey(
        ForumPost, 
        on_delete=models.CASCADE, 
        related_name='comments',
        verbose_name="Postingan Terkait"
    )
    content = models.TextField(verbose_name="Isi Komentar")
    commented_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='forum_comments',
        verbose_name="Dikomentari Oleh"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Komentar"
        verbose_name_plural = "Komentar"
        ordering = ['created_at']
        
    def __str__(self):
        return f"Komentar dari {self.commented_by.username} pada {self.post.title[:30]}..."


# ==============================================================================
# 4. Model Vote (Like/Dislike) - TIDAK BERUBAH
# ==============================================================================
class Vote(models.Model):
    post = models.ForeignKey(
        ForumPost, 
        on_delete=models.CASCADE, 
        related_name='votes',
        verbose_name="Postingan yang divote"
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='post_votes',
        verbose_name="Pengguna"
    )
    vote_type = models.SmallIntegerField(
        choices=VOTE_CHOICES,
        verbose_name="Tipe Vote"
    )
    
    class Meta:
        verbose_name = "Vote Postingan"
        verbose_name_plural = "Vote Postingan"
        unique_together = ('post', 'user') 
        
    def __str__(self):
        vote_status = "Like" if self.vote_type == 1 else "Dislike"
        return f"{self.user.username} memberikan {vote_status} pada {self.post.title[:30]}..."