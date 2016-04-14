# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 18:52
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nome')),
                ('content', models.TextField(help_text='Breve descri\xe7\xe3o da receita', verbose_name='Conte\xfado')),
                ('ingredients', models.TextField(verbose_name='Ingredientes')),
                ('method_of_preparation', models.TextField(verbose_name='Modo de preparo')),
                ('time_of_preparation', models.CharField(max_length=20, verbose_name='Tempo de preparo')),
                ('produce', models.CharField(max_length=20, verbose_name='Redimento')),
                ('image', models.ImageField(blank=True, null=True, upload_to='/uploads/post/images', verbose_name='Foto')),
                ('featured_image', image_cropping.fields.ImageRatioField('photo', '260x140', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='featured image')),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('status', models.BooleanField(default=True)),
                ('published_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Data de Publicacao')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
            },
        ),
    ]
