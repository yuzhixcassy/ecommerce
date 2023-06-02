# Generated by Django 4.2.1 on 2023-06-02 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('razor_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razor_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('razor_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('oreder_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Acc', 'Accepted'), ('Packed', 'Packed'), ('OTW', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='Pending', max_length=50)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.barang')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('payment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.payment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]