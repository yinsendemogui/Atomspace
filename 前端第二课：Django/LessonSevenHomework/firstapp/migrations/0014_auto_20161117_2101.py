# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0013_auto_20161117_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover_image',
            field=models.FileField(blank=True, null=True, upload_to='/upload/cover_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.FileField(upload_to='/upload/profile_image'),
        ),
    ]
