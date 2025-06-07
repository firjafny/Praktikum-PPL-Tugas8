from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama', 'deskripsi', 'harga', 'stok', 'kategori', 'gambar']
