# Generated by Django 3.2.9 on 2024-05-18 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('birth_day', models.DateTimeField(verbose_name='Дата рождения')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('adres', models.CharField(max_length=200, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=200, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=200, verbose_name='E-mail')),
                ('discount', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]