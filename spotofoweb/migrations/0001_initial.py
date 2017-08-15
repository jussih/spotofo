# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-15 20:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spid', models.CharField(max_length=2048)),
                ('name', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='MqttTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=2048)),
                ('username', models.CharField(max_length=2048)),
                ('host', models.CharField(max_length=2048)),
                ('port', models.IntegerField()),
                ('password', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spid', models.CharField(max_length=2048)),
                ('spuser', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='SpotifyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=2048)),
                ('token_info', models.CharField(blank=True, max_length=2048, null=True)),
                ('devices', models.ManyToManyField(blank=True, related_name='users', to='spotofoweb.Device')),
                ('playlists', models.ManyToManyField(blank=True, related_name='users', to='spotofoweb.Playlist')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spotify', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User',
            },
        ),
    ]