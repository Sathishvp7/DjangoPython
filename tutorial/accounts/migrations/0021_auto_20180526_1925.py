# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-26 13:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20180526_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='user',
        ),
        migrations.AlterField(
            model_name='blogs',
            name='actual_start_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 26, 19, 25, 28, 856664)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2018, 5, 26, 19, 25, 28, 856664)),
        ),
    ]