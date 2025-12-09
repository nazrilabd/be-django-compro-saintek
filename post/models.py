from django.db import models
from django.utils.text import slugify
# --- IMPORT PENTING BARU ---
from django.contrib.auth.models import User 

# Model untuk Tag (Daftar Tag) - TIDAK BERUBAH
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    # ... (metode dan Meta lainnya)
    def __str__(self):
        return self.name

# Model untuk Postingan Blog - DITAMBAH FIELD created_by
class Post(models.Model):
    # --- FIELD BARU: Created By ---
    created_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,        # Jika user dihapus, postingan ikut dihapus
        related_name='blog_posts',      # Nama terbalik untuk mengakses post dari user
        verbose_name="Dibuat Oleh"
    )
    
    # --- Data Utama Postingan (Dari sebelumnya) ---
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def save(self, *args, **kwargs):
        # ... (logika slugify)
        if not self.slug or (self.slug != slugify(self.title) and self.pk is None):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ['-created_at'] 
        
    def __str__(self):
        return self.title