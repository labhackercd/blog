# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 15:58
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20160415_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Conte\xfado'),
        ),
    ]
