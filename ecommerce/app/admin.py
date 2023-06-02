from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Barang)
class BarangModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'kategori', 'harga', 'deskripsi', 'foto']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'daerah', 'kota', 'negara', 'kodepos']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'barang', 'qty']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'razor_order_id', 'razor_payment_status', 'razor_payment_id', 'paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'barang', 'qty', 'ordered_date', 'status', 'payment']

# @admin.register(Wishlist)
# class WishlistModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'barang']