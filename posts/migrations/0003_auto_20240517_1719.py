# Generated by Django 3.2.9 on 2024-05-17 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20240517_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flower',
            options={'verbose_name': 'Цветы', 'verbose_name_plural': 'Цветы'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': 'Поставщиков', 'verbose_name_plural': 'Поставщики'},
        ),
    ]
