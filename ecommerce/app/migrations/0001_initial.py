# Generated by Django 4.2.1 on 2023-05-29 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_brg', models.CharField(max_length=50)),
                ('jenis_brg', models.CharField(max_length=15)),
                ('harga_brg', models.FloatField()),
                ('foto_brg', models.ImageField(upload_to='product')),
            ],
        ),
    ]