# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-28 08:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180428_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='actual_date_completion',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='actual_start_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 28, 13, 55, 53, 278690)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2018, 4, 28, 13, 55, 53, 278690)),
        ),
    ]