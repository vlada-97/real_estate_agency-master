# Generated by Django 4.2.2 on 2023-06-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_flat_has_balcony_alter_flat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.CharField(blank=True, choices=[(None, 'Неизвестно'), (True, 'Новостройка'), (False, 'Старое здание')], db_index=True, max_length=20, null=True, verbose_name='Состояние здания'),
        ),
    ]
