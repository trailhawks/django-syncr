# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_time', models.DateTimeField()),
                ('twitter_id', models.BigIntegerField(unique=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('screen_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
                ('location', models.CharField(max_length=50, null=True, blank=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('thumbnail_url', models.URLField()),
                ('url', models.URLField(null=True, blank=True)),
                ('followers', models.ManyToManyField(related_name='followers_user_set', null=True, to='twitter.TwitterUser', blank=True)),
                ('friends', models.ManyToManyField(related_name='friends_user_set', null=True, to='twitter.TwitterUser', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(to='twitter.TwitterUser'),
            preserve_default=True,
        ),
    ]
