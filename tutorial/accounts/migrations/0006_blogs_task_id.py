# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-04 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180304_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='task_id',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]