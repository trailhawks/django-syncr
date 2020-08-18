# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=50)),
                ('sync_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flickr_id', models.BigIntegerField(unique=True)),
                ('owner', models.CharField(max_length=50)),
                ('owner_nsid', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(help_text=b'Automatically built from the title.', max_length=100, unique_for_date=b'taken_date')),
                ('description', models.TextField(blank=True)),
                ('taken_date', models.DateTimeField()),
                ('upload_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('photopage_url', models.URLField()),
                ('farm', models.PositiveSmallIntegerField()),
                ('server', models.PositiveSmallIntegerField()),
                ('secret', models.CharField(max_length=10)),
                ('original_secret', models.CharField(max_length=10, blank=True)),
                ('large_square_width', models.PositiveSmallIntegerField(null=True)),
                ('large_square_height', models.PositiveSmallIntegerField(null=True)),
                ('thumbnail_width', models.PositiveSmallIntegerField()),
                ('thumbnail_height', models.PositiveSmallIntegerField()),
                ('small_width', models.PositiveSmallIntegerField()),
                ('small_height', models.PositiveSmallIntegerField()),
                ('medium_width', models.PositiveSmallIntegerField(null=True)),
                ('medium_height', models.PositiveSmallIntegerField(null=True)),
                ('medium_640_width', models.PositiveSmallIntegerField(null=True)),
                ('medium_640_height', models.PositiveSmallIntegerField(null=True)),
                ('large_width', models.PositiveSmallIntegerField(null=True)),
                ('large_height', models.PositiveSmallIntegerField(null=True)),
                ('original_width', models.PositiveSmallIntegerField()),
                ('original_height', models.PositiveSmallIntegerField()),
                ('enable_comments', models.BooleanField(default=True)),
                ('license', models.CharField(max_length=50, choices=[(b'0', b'All Rights Reserved'), (b'1', b'Attribution-NonCommercial-ShareAlike License'), (b'2', b'Attribution-NonCommercial License'), (b'3', b'Attribution-NonCommercial-NoDerivs License'), (b'4', b'Attribution License'), (b'5', b'Attribution-ShareAlike License'), (b'6', b'Attribution-NoDerivs License')])),
                ('geo_latitude', models.FloatField(null=True, blank=True)),
                ('geo_longitude', models.FloatField(null=True, blank=True)),
                ('geo_accuracy', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('geo_locality', models.CharField(max_length=200, null=True, blank=True)),
                ('geo_county', models.CharField(max_length=200, null=True, blank=True)),
                ('geo_region', models.CharField(max_length=200, null=True, blank=True)),
                ('geo_country', models.CharField(max_length=200, null=True, blank=True)),
                ('exif_make', models.CharField(max_length=50, blank=True)),
                ('exif_model', models.CharField(max_length=50, blank=True)),
                ('exif_orientation', models.CharField(max_length=50, blank=True)),
                ('exif_exposure', models.CharField(max_length=50, blank=True)),
                ('exif_software', models.CharField(max_length=50, blank=True)),
                ('exif_aperture', models.CharField(max_length=50, blank=True)),
                ('exif_iso', models.CharField(max_length=50, blank=True)),
                ('exif_metering_mode', models.CharField(max_length=50, blank=True)),
                ('exif_flash', models.CharField(max_length=50, blank=True)),
                ('exif_focal_length', models.CharField(max_length=50, blank=True)),
                ('exif_color_space', models.CharField(max_length=50, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-taken_date',),
                'get_latest_by': 'upload_date',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('flickr_id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('author_nsid', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField()),
                ('permanent_url', models.URLField()),
                ('comment', models.TextField()),
                ('photo', models.ForeignKey(to='flickr.Photo', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ('pub_date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotoSet',
            fields=[
                ('flickr_id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('owner', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('photos', models.ManyToManyField(to='flickr.Photo')),
                ('primary', models.ForeignKey(related_name='primary_photo_set', default=None, on_delete=models.CASCADE, to='flickr.Photo', null=True)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='favoritelist',
            name='photos',
            field=models.ManyToManyField(to='flickr.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favoritelist',
            name='primary',
            field=models.ForeignKey(related_name='primary_in', to='flickr.Photo', on_delete=models.CASCADE, null=True),
            preserve_default=True,
        ),
    ]
