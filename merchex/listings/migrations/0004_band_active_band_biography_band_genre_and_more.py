# Generated by Django 4.1.1 on 2022-10-08 10:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_description_listing_sold_listing_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='band',
            name='biography',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock')], default='HH', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='official_home_page',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
