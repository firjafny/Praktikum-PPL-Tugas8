from django.db import models

class Produk(models.Model):
    KATEGORI_CHOICES = [
        ('kue kering', 'Kue Kering'),
        ('kue basah', 'Kue Basah'),
        ('roti', 'Roti'),
        ('spesial', 'Spesial'),
    ]

    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()
    kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES, default='lainnya')
    gambar = models.ImageField(upload_to='gambar_produk/', blank=True, null=True)


    def __str__(self):
        return self.nama
