# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-26 12:29
from __future__ import unicode_literals

import datetime
import django.contrib.auth
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20180524_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='actual_start_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 26, 17, 59, 31, 295365)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2018, 5, 26, 17, 59, 31, 295365)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='user',
            field=models.CharField(default=django.contrib.auth.get_user_model, max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]
