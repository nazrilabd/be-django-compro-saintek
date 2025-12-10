from django.db import models
from django.contrib.auth.models import User 

class HeaderContent(models.Model):
    title = models.CharField(max_length=150, verbose_name='Judul Header')
    
    # --- DESKRIPSI BARU ---
    description_short = models.TextField(verbose_name='Deskripsi Singkat (Ringkasan)')
    description_full = models.TextField(verbose_name='Deskripsi Lengkap')
    
    image = models.ImageField(
        upload_to='header_images/', 
        blank=True, 
        null=True,
        verbose_name='Gambar Header'
    )
    
    created_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='header_contents',
        verbose_name='Dibuat Oleh'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Konten Header'
        verbose_name_plural = 'Konten Header'

    def __str__(self):
        return self.title