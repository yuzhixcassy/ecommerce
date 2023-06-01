# Generated by Django 4.2.1 on 2023-05-31 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('daerah', models.CharField(max_length=200)),
                ('kota', models.CharField(max_length=50)),
                ('notelp', models.IntegerField(default=0)),
                ('kodepos', models.IntegerField()),
                ('negara', models.CharField(choices=[('Afghanistan', 'Afghanistan'), ('Armenia', 'Armenia'), ('Azerbaijan', 'Azerbaijan'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Bhutan', 'Bhutan'), ('Brunei', 'Brunei'), ('Kamboja', 'Kamboja'), ('Cina', 'Cina'), ('Siprus', 'Siprus'), ('Timor Leste', 'Timor Leste'), ('Georgia', 'Georgia'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Irak', 'Irak'), ('Israel', 'Israel'), ('Jepang', 'Jepang'), ('Yordania', 'Yordania'), ('Kazakhstan', 'Kazakhstan'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Lebanon', 'Lebanon'), ('Malaysia', 'Malaysia'), ('Maladewa', 'Maladewa'), ('Mongolia', 'Mongolia'), ('Myanmar', 'Myanmar'), ('Nepal', 'Nepal'), ('Korea Utara', 'Korea Utara'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palestina', 'Palestina'), ('Filipina', 'Filipina'), ('Qatar', 'Qatar'), ('Arab Saudi', 'Arab Saudi'), ('Singapura', 'Singapura'), ('Korea Selatan', 'Korea Selatan'), ('Sri Lanka', 'Sri Lanka'), ('Suriah', 'Suriah'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Thailand', 'Thailand'), ('Turki', 'Turki'), ('Turkmenistan', 'Turkmenistan'), ('Uni Emirat Arab', 'Uni Emirat Arab'), ('Uzbekistan', 'Uzbekistan'), ('Vietnam', 'Vietnam'), ('Yaman', 'Yaman')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
