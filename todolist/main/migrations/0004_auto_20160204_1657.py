# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160204_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
