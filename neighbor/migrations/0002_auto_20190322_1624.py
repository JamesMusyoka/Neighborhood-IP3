# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-22 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighbor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='neighborhood',
            options={'ordering': ['neighborhood_name']},
        ),
        migrations.AddField(
            model_name='business',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]