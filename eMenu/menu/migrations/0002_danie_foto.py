# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='danie',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
