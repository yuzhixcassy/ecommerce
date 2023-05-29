# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('kategori/', views.KategoriV.as_view(), name='kategori'),
]