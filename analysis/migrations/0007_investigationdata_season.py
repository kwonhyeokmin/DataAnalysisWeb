# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-09 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0006_auto_20171229_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigationdata',
            name='season',
            field=models.IntegerField(default=0),
        ),
    ]
