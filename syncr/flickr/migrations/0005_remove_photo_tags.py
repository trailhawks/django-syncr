# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 00:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flickr', '0004_auto_20180717_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='tags',
        ),
    ]