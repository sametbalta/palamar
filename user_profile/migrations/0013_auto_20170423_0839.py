# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-23 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0012_auto_20170423_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='selected_site',
            field=models.IntegerField(null=True),
        ),
    ]
