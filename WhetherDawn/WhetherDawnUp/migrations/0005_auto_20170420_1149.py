# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WhetherDawnUp', '0004_coords_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coords',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
