# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-02 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemPic',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]
