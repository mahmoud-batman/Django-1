# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-14 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20181114_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['-updated'], 'permissions': (('can_update', 'can update'),)},
        ),
    ]