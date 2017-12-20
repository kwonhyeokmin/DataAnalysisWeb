# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20171201_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='fruit_n',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='datafile',
            unique_together=set([('date', 'sampleNo')]),
        ),
    ]
