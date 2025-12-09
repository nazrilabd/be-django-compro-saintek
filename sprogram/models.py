from django.db import models

class ProgramStudi(models.Model):
    # --- Informasi Program Studi (Prodi) ---
    
    # Nama Program Studi (Misalnya: Teknik Informatika, Manajemen)
    name_programstudy = models.CharField(
        max_length=150, 
        verbose_name="Nama Program Studi"
    )
    
    # Deskripsi Singkat/Tentang Prodi
    about_programstudy = models.TextField(
        verbose_name="Tentang Program Studi"
    )
    
    # Gambar Header/Cover Utama Prodi
    cover_header = models.ImageField(
        upload_to='prodi_covers/', 
        blank=True, 
        null=True,
        verbose_name="Cover Header Prodi (Gambar)"
    )
    
    # --- Informasi Himpunan Mahasiswa (HIMA) ---
    
    # Nama Himpunan Mahasiswa (Misalnya: HIMATIF)
    name_hima = models.CharField(
        max_length=150,
        verbose_name="Nama Himpunan Mahasiswa"
    )
    
    # Cover/Logo HIMA
    cover_hima = models.ImageField(
        upload_to='hima_covers/', 
        blank=True, 
        null=True,
        verbose_name="Cover/Logo HIMA (Gambar)"
    )
    
    # Deskripsi Singkat Tentang HIMA
    description_hima = models.TextField(
        verbose_name="Deskripsi HIMA"
    )
    
    # --- Informasi Kepala Program Studi (Kaprodi) ---
    
    # Foto Profil Kaprodi
    kaprodi_profile = models.ImageField(
        upload_to='kaprodi_profiles/', 
        blank=True, 
        null=True,
        verbose_name="Foto Profil Kaprodi (Gambar)"
    )
    
    # Nama Lengkap Kaprodi
    kaprodi_name = models.CharField(
        max_length=100,
        verbose_name="Nama Kaprodi"
    )
    
    # Deskripsi/Bio Singkat Kaprodi (atau Jabatan/Pendidikan)
    kaprodi_description = models.TextField(
        verbose_name="Deskripsi Kaprodi"
    )

    class Meta:
        # Nama tampilan di Django Admin (plural)
        verbose_name_plural = "Daftar Program Studi"
        # Nama tampilan di Django Admin (singular)
        verbose_name = "Program Studi"
        
    def __str__(self):
        # Representasi string objek (untuk admin)
        return self.name_programstudy