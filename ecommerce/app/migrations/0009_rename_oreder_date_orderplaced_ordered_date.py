# Generated by Django 4.2.1 on 2023-06-02 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_payment_orderplaced'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='oreder_date',
            new_name='ordered_date',
        ),
    ]