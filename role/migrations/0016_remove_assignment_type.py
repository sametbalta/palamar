# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-20 17:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0015_auto_20170420_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='type',
        ),
    ]