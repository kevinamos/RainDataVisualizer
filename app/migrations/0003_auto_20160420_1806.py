# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 18:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160420_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyWeatherByCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=50)),
                ('boston_temp', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('houston_temp', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.AlterField(
            model_name='raindatastore',
            name='Amount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='raindatastore',
            name='County',
            field=models.CharField(choices=[('Busia', ' Busia County\n'), ('Bomet', ' Bomet county\n'), ('Nairobi', ' Nairobi County\n'), ('Kisumu', ' Kisumu County\n'), ('Mombasa', ' Mombasa County\n')], max_length=50),
        ),
    ]
