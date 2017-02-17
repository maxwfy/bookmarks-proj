# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('is_public', models.BooleanField(default=True, verbose_name='public')),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_updated', models.DateTimeField(verbose_name='date updated')),
                ('owner', models.ForeignKey(related_name='bookmarks', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name_plural': 'bookmarks',
                'ordering': ['-date_created'],
                'verbose_name': 'bookmark',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'tags',
                'ordering': ['name'],
                'verbose_name': 'tag',
            },
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(to='marcador.Tag', blank=True),
        ),
    ]
