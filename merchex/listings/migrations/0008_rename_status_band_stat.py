# Generated by Django 4.1.1 on 2022-10-11 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_band_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='band',
            old_name='status',
            new_name='stat',
        ),
    ]
