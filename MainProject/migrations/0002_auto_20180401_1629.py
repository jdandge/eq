# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-01 16:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registeredUser',
            new_name='AppUser',
        ),
    ]