from django.contrib import admin
from . models import Barang

# Register your models here.
@admin.register(Barang)
class BarangModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama_brg', 'jenis_brg', 'harga_brg', 'foto_brg']