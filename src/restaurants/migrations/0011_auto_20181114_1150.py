# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-14 11:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_auto_20181114_1149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['-updated'], 'permissions': (('can_read', 'can read seko seko'),)},
        ),
    ]
