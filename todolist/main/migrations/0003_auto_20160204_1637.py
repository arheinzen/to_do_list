# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_todolist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
