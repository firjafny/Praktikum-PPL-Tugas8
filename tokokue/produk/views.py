from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm
from django.contrib import messages

def daftar_produk(request):
    semua_produk = Produk.objects.all()
    return render(request, 'produk/list.html', {'produk': semua_produk})

def tambah_produk(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST, request.FILES)  # <== Tambahkan request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil ditambahkan!')
            return redirect('daftar_produk')
    else:
        form = ProdukForm()
    return render(request, 'produk/form.html', {'form': form, 'judul': 'Tambah Produk'})

def edit_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, request.FILES, instance=produk)  # <== Tambahkan request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil diperbarui!')
            return redirect('daftar_produk')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'produk/form.html', {'form': form, 'judul': 'Edit Produk'})

def hapus_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    produk.delete()
    messages.success(request, 'Produk berhasil dihapus!')
    return redirect('daftar_produk')
