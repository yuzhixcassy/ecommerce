from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.views import View
from django.db.models import Count
from . models import *
from . forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def tentang(request):
    return render(request, 'app/tentang.html')

def kontak(request):
    return render(request, 'app/kontak.html')

class KategoriV(View):
    def get(self, request, val):
        barang = Barang.objects.filter(kategori=val)
        nama = Barang.objects.filter(kategori=val).values('nama')#.annotate(total=Count('nama'))
        return render(request, 'app/kategori.html', locals())

class KategoriNama(View):
    def get(self, request, val):
        barang = Barang.objects.filter(nama=val)
        nama = Barang.objects.filter(kategori=barang[0].kategori).values('nama')#.annotate(total=Count('nama'))
        return render(request, 'app/kategori.html', locals())

class DetilBarang(View):
    def get(self, request, pk):
        barang = Barang.objects.get(pk=pk)
        return render(request, 'app/detil_barang.html', locals())
    
class RegistrasiCustV(View):
    def get(self, request):
        form = CustomerRegistForm()
        return render(request, 'app/registrasicust.html', locals())
    def post(self, request):
        form = CustomerRegistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun berhasil dibuat!")
        else:
            messages.warning(request, "Invalid data")
        return render(request, 'app/registrasicust.html', locals())

class ProfileV(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'app/profile.html', locals())
    def post(self, request):
        return render(request, 'app/profile.html', locals())