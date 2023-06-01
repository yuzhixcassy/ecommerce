from django.db import models
from django.contrib.auth.models import User

# Create your models here.

KATEGORI_CHOICES = (
    ('PKN', 'Pakaian'),
    ('CLN', 'Celana'),
    ('SPT', 'Sepatu'),
    ('AKS', 'Aksesoris'),
)
class Barang(models.Model):
    nama = models.CharField(max_length=50, null=False)
    kategori = models.CharField(choices=KATEGORI_CHOICES, null=False, max_length=15)
    harga = models.FloatField(null=False)
    deskripsi = models.TextField(null = False)
    foto = models.ImageField(upload_to='product', null=False)
    def __str__(self):
        return self.nama

STATE_CHOICES = [
('Afghanistan', 'Afghanistan'),
('Armenia', 'Armenia'),
('Azerbaijan', 'Azerbaijan'),
('Bahrain', 'Bahrain'),
('Bangladesh', 'Bangladesh'),
('Bhutan', 'Bhutan'),
('Brunei', 'Brunei'),
('Kamboja', 'Kamboja'),
('Cina', 'Cina'),
('Siprus', 'Siprus'),
('Timor Leste', 'Timor Leste'),
('Georgia', 'Georgia'),
('India', 'India'),
('Indonesia', 'Indonesia'),
('Iran', 'Iran'),
('Irak', 'Irak'),
('Israel', 'Israel'),
('Jepang', 'Jepang'),
('Yordania', 'Yordania'),
('Kazakhstan', 'Kazakhstan'),
('Kuwait', 'Kuwait'),
('Kyrgyzstan', 'Kyrgyzstan'),
('Laos', 'Laos'),
('Lebanon', 'Lebanon'),
('Malaysia', 'Malaysia'),
('Maladewa', 'Maladewa'),
('Mongolia', 'Mongolia'),
('Myanmar', 'Myanmar'),
('Nepal', 'Nepal'),
('Korea Utara', 'Korea Utara'),
('Oman', 'Oman'),
('Pakistan', 'Pakistan'),
('Palestina', 'Palestina'),
('Filipina', 'Filipina'),
('Qatar', 'Qatar'),
('Arab Saudi', 'Arab Saudi'),
('Singapura', 'Singapura'),
('Korea Selatan', 'Korea Selatan'),
('Sri Lanka', 'Sri Lanka'),
('Suriah', 'Suriah'),
('Taiwan', 'Taiwan'),
('Tajikistan', 'Tajikistan'),
('Thailand', 'Thailand'),
('Turki', 'Turki'),
('Turkmenistan', 'Turkmenistan'),
('Uni Emirat Arab', 'Uni Emirat Arab'),
('Uzbekistan', 'Uzbekistan'),
('Vietnam', 'Vietnam'),
('Yaman', 'Yaman')
]
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200)
    daerah = models.CharField(max_length=200)
    kota = models.CharField(max_length=50)
    notelp = models.IntegerField(default=0)
    kodepos = models.IntegerField()
    negara = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.nama

