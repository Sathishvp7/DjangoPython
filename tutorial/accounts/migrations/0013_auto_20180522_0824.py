# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-22 02:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20180429_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='actual_start_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 22, 8, 24, 55, 904848)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2018, 5, 22, 8, 24, 55, 904848)),
        ),
    ]