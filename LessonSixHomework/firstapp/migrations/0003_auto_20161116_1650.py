# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20161116_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='avatar',
            field=models.CharField(default='http://semantic-ui.com/images/avatar/small/matt.jpg', max_length=50),
        ),
    ]