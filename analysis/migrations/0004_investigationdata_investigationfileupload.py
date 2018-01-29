# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_auto_20171228_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestigationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('day', models.IntegerField(default=0)),
                ('sampleNo', models.FloatField(default=0)),
                ('stem_width', models.FloatField(default=0)),
                ('plent_len', models.FloatField(default=0)),
                ('fcluster_n', models.FloatField(default=0)),
            ],
            options={
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='InvestigationfileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
