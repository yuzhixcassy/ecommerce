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
    path('profile/>', views.ProfileV.as_view(), name='profile'),
    path('address/>', views.ProfileV.as_view(), name='address'),

    path('registration/', views.RegistrasiCustV.as_view(), name='registrasicust'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form = LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class = ResetPasswordForm), name='password_reset'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)