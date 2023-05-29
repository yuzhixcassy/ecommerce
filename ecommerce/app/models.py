from django.db import models

# Create your models here.

JENIS_CHOICES = (
    ('PAKAIAN', 'Pakaian'),
    ('CELANA', 'Celana'),
    ('SEPATU', 'Sepatu'),
    ('AKSESORIS', 'Aksesoris'),
)
class Barang(models.Model):
    nama_brg = models.CharField(max_length=50, null=False)
    jenis_brg = models.CharField(choices=JENIS_CHOICES, null=False, max_length=15)
    harga_brg = models.FloatField(null=False)
    deskripsi = models.TextField(null = False)
    foto_brg = models.ImageField(upload_to='product', null=False)
    # keterangan = models.TextField()
    def __str__(self):
        return self.nama_brg
