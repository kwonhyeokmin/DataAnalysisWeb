# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('week', models.CharField(default='', max_length=2)),
                ('sampleNo', models.PositiveIntegerField(default=0)),
                ('location', models.CharField(default='', max_length=20)),
                ('plant_len', models.FloatField(default=0)),
                ('stem_width', models.FloatField(default=0)),
                ('leaf_len', models.FloatField(default=0)),
                ('leaf_width', models.FloatField(default=0)),
                ('leaf_n', models.FloatField(default=0)),
                ('group_blossoming', models.FloatField(default=0)),
                ('group_fruit', models.FloatField(default=0)),
                ('group_harvest', models.FloatField(default=0)),
                ('ped', models.FloatField(default=0)),
                ('light', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='fileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
