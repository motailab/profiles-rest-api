# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilefeeditem',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profilefeeditem',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
