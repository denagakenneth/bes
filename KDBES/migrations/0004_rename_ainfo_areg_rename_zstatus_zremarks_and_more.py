# Generated by Django 4.0.4 on 2022-05-16 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KDBES', '0003_rename_bbevents_bevent_bcategory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ainfo',
            new_name='Areg',
        ),
        migrations.RenameModel(
            old_name='Zstatus',
            new_name='Zremarks',
        ),
        migrations.RenameField(
            model_name='zremarks',
            old_name='status',
            new_name='zdate',
        ),
    ]
