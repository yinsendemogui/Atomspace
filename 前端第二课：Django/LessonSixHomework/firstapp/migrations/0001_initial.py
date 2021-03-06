# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='chensiqi', max_length=10)),
                ('comment', models.TextField(max_length=500)),
                ('avatar', models.CharField(default='http://semantic-ui.com/images/avatar/small/matt.jpg', max_length=50)),
                ('createtime', models.DateField(auto_now=True)),
            ],
        ),
    ]
