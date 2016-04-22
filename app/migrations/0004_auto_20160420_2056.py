# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160420_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyweatherbycity',
            name='boston_temp',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='monthlyweatherbycity',
            name='houston_temp',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='monthlyweatherbycity',
            name='month',
            field=models.IntegerField(),
        ),
    ]
