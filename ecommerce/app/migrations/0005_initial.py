# Generated by Django 4.2.1 on 2023-05-30 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0004_delete_barang'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('kategori', models.CharField(choices=[('PKN', 'Pakaian'), ('CLN', 'Celana'), ('SPT', 'Sepatu'), ('AKS', 'Aksesoris')], max_length=15)),
                ('harga', models.FloatField()),
                ('deskripsi', models.TextField()),
                ('foto', models.ImageField(upload_to='product')),
            ],
        ),
    ]
