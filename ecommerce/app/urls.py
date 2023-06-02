# from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import *

urlpatterns = [
    path('', views.home),
    path('tentang/', views.tentang, name='tentang'),
    path('kontak/', views.kontak, name='kontak'),
    path('kategori/<slug:val>', views.KategoriV.as_view(), name='kategori'),
    path('kategori_nama/<val>', views.KategoriNama.as_view(), name='kategori_nama'),
    path('detil_barang/<slug:pk>', views.DetilBarang.as_view(), name='detil_barang'),
    path('profile/', views.ProfileV.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('updateaddress/<int:pk>', views.UpdateAddress.as_view(), name='updateaddress'),
    path('updateaddress/delete/<int:pk>', views.DeleteAddress.as_view(), name='deleteaddress'),
    path('search/', views.search, name='search'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout/', views.checkout.as_view(), name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('orders/', views.orders, name='orders'),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),

    path('registration/', views.RegistrasiCustV.as_view(), name='registrasicust'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form = LoginForm), name='login'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class = PasswordChangeForm, success_url = '/passwordchangedone'), name='passwordchange'),
#   path('passwordchangedone/', PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='password_changed_done'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class = ResetPasswordForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class = SetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)