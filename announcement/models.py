from django.db import models
from django.contrib.auth.models import User 

class Announcement(models.Model):
    # Field wajib
    created_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='announcements',
        verbose_name='Dibuat Oleh'
    )
    title = models.CharField(max_length=255, verbose_name='Judul Pengumuman')
    description = models.TextField(verbose_name='Isi Pengumuman')

    # Field otomatis
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Waktu Dibuat')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Waktu Diperbarui')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Pengumuman'
        verbose_name_plural = 'Pengumuman'

    def __str__(self):
        return self.title