# Generated by Django 4.2.2 on 2023-06-26 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20230626_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
