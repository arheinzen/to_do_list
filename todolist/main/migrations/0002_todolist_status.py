# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
