# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloud',
            name='QQ',
        ),
        migrations.RemoveField(
            model_name='cloud',
            name='wechat',
        ),
        migrations.AlterField(
            model_name='cloud',
            name='QQ_group',
            field=models.IntegerField(max_length=32, verbose_name='响应QQ群'),
        ),
        migrations.AlterField(
            model_name='cloud',
            name='phone',
            field=models.CharField(max_length=32, verbose_name='联系电话'),
        ),
    ]