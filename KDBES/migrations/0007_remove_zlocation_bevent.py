# Generated by Django 4.0.4 on 2022-06-26 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KDBES', '0006_rename_bcategory_bevent_bmainevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zlocation',
            name='bevent',
        ),
    ]