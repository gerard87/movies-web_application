# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 13:26
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0004_auto_20160414_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='country',
        ),
        migrations.RemoveField(
            model_name='company',
            name='country',
        ),
        migrations.RemoveField(
            model_name='director',
            name='country',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_release_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='actor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='director',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]