from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Barang)
class BarangModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'kategori', 'harga', 'deskripsi', 'foto']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'daerah', 'kota', 'negara', 'kodepos']