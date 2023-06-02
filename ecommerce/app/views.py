from django.shortcuts import render, redirect
from urllib import request
from django.http import JsonResponse
from django.views import View
from django.db.models import *
from . models import *
from . forms import *
from django.contrib import messages
import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def home(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/home.html', locals())

@login_required
def search(request):
    query = request.GET['search']
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    barang = Barang.objects.filter(Q(nama__icontains=query))
    return render(request, 'app/search.html', locals())

@login_required
def tentang(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/tentang.html', locals())

@login_required
def kontak(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/kontak.html', locals())

@method_decorator(login_required, name='dispatch')
class KategoriV(View):
    def get(self, request, val):
        totalitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
        barang = Barang.objects.filter(kategori=val)
        nama = Barang.objects.filter(kategori=val).values('nama')
        return render(request, 'app/kategori.html', locals())

@method_decorator(login_required, name='dispatch')
class KategoriNama(View):
    def get(self, request, val):
        barang = Barang.objects.filter(nama=val)
        nama = Barang.objects.filter(kategori=barang[0].kategori).values('nama')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/kategori.html', locals())
    
@method_decorator(login_required, name='dispatch')
class DetilBarang(View):
    def get(self, request, pk):
        barang = Barang.objects.get(pk=pk)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/detil_barang.html', locals())

class RegistrasiCustV(View):
    def get(self, request):
        form = CustomerRegistForm()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/registrasicust.html', locals())
    def post(self, request):
        form = CustomerRegistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun berhasil dibuat!")
        else:
            messages.warning(request, "Invalid data")
        return render(request, 'app/registrasicust.html', locals())

@method_decorator(login_required, name='dispatch')
class ProfileV(View):
    def get(self, request):
        form = ProfileForm(request.POST)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html', locals())
    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            nama = form.cleaned_data['nama']
            daerah = form.cleaned_data['daerah']
            kota = form.cleaned_data['kota']
            notelp = form.cleaned_data['notelp']
            negara = form.cleaned_data['negara']
            kodepos = form.cleaned_data['kodepos']

            reg = Customer(user=user, nama=nama, daerah=daerah, kota=kota, notelp=notelp, negara=negara, kodepos=kodepos)
            reg.save()
            messages.success(request, "Profil berhasil diperbarui!")
        else:
            messages.warning(request, "Profil gagal diperbarui")
        return render(request, 'app/profile.html', locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/address.html', locals())

@method_decorator(login_required, name='dispatch')
class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = ProfileForm(instance=add)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/updateaddress.html', locals())

@method_decorator(login_required, name='dispatch')
class DeleteAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        add.delete()
        return redirect('address')
    
    def post(self, request, pk):
        form = ProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.nama = form.cleaned_data['nama']
            add.daerah = form.cleaned_data['daerah']
            add.kota = form.cleaned_data['kota']
            add.notelp = form.cleaned_data['notelp']
            add.negara = form.cleaned_data['negara']
            add.kodepos = form.cleaned_data['kodepos']
            add.save()
            messages.success(request, "Profil berhasil diupdate!")
        else:
            messages.warning(request, "gagal update")
        return render(request, 'app/updateaddress.html', locals())
    
@login_required
def add_to_cart(request):
    user = request.user
    barang_id = request.GET.get('prod_id')
    barang = Barang.objects.get(id=barang_id)
    Cart(user=user, barang=barang).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.qty * p.barang.harga
        amount = amount + value
    totalamount = amount + 15.000
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/addtocart.html', locals())

@method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self, request):
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        for p in cart_items:
            value = p.qty * p.barang.harga
            famount = famount + value
        totalamount = famount + 15.000
        razoramount = int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = { "amount": razoramount, "currency": "IDR", "receipt": "order_rcptid_11" }
        payment_response = client.order.create(data=data)
        print(payment_response)
        # {'id': 'order_LwwSpgZ6DIJ5Uu', 'entity': 'order', 'amount': 6098, 'amount_paid': 0, 'amount_due': 6098, 'currency': 'IDR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1685682835}
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user = user,
                amount = totalamount,
                razor_order_id = order_id,
                razor_payment_status = order_status,
            )
            payment.save()
        return render(request, 'app/checkout.html', locals())

@login_required
def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    user = request.user
    cutomer = Customer.objects.get(id=cust_id)
    payment = Payment.objects.get(razor_order_id=order_id)
    payment.paid = True
    payment.razor_payment_id = payment_id
    payment.save()
    cart = Cart.objects.filter(user=user)
    
    for c in cart:
        OrderPlaced(user=user, cutomer=cutomer, barang=c.barang, qty = c.qty, payment=payment).save()
        c.delete()
    return redirect('orders')

@login_required
def orders(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.filter(Q(barang=prod_id) & Q(user=request.user)).first()
        c.qty +=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.qty * p.barang.harga
            amount = amount + value
        totalamount = amount + 15.000
        # print(prod_id)
        data = {
            'qty' : c.qty,
            'amount' : amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.filter(Q(barang=prod_id) & Q(user=request.user)).first()
        c.qty -=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.qty * p.barang.harga
            amount = amount + value
        totalamount = amount + 15.000
        # print(prod_id)
        data = {
            'qty' : c.qty,
            'amount' : amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.filter(Q(barang=prod_id) & Q(user=request.user)).first()
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.qty * p.barang.harga
            amount = amount + value
        totalamount = amount + 15.000
        data = {
            'amount' : amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)