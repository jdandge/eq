# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-18 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0005_auto_20180415_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='timeslot_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='timeslot_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='timestamp',
            field=models.DateField(blank=True, null=True),
        ),
    ]
