# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotofoweb', '0002_play'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='timestamp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='play',
            name='device_type',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='play',
            name='username',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='play',
            name='volume_percent',
            field=models.IntegerField(),
        ),
        migrations.AddIndex(
            model_name='play',
            index=models.Index(fields=['user', 'device', 'timestamp'], name='spotofoweb__user_id_379c48_idx'),
        ),
    ]
