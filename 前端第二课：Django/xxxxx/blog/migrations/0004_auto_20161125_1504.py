# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 07:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]
