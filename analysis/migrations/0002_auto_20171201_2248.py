# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datafile',
            options={'ordering': ['date']},
        ),
        migrations.AlterUniqueTogether(
            name='datafile',
            unique_together=set([('date', 'week', 'sampleNo', 'location', 'plant_len', 'stem_width', 'leaf_len', 'leaf_width', 'leaf_n', 'group_blossoming', 'group_fruit', 'group_harvest', 'ped', 'light')]),
        ),
    ]
