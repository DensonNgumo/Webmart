# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='paymentdetails',
            options={'verbose_name_plural': 'paymentDetails'},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='Default product description'),
        ),
    ]
