# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20161114_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='comment',
            name='avatar',
            field=models.CharField(default='static/images/default.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
