# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-16 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flickr', '0002_photo_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='license',
            field=models.CharField(choices=[('0', 'All Rights Reserved'), ('1', 'Attribution-NonCommercial-ShareAlike License'), ('2', 'Attribution-NonCommercial License'), ('3', 'Attribution-NonCommercial-NoDerivs License'), ('4', 'Attribution License'), ('5', 'Attribution-ShareAlike License'), ('6', 'Attribution-NoDerivs License')], max_length=50),
        ),
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=models.SlugField(help_text='Automatically built from the title.', max_length=100, unique_for_date='taken_date'),
        ),
    ]