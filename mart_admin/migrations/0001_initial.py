# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 17:48
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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=150)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_mobile_number', models.CharField(max_length=14)),
                ('customer_address', models.CharField(max_length=250)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('order_date_time', models.DateTimeField(auto_now=True)),
                ('payment_method', models.CharField(choices=[('debit', 'Debit Card'), ('mpesa', 'MPESA'), ('cash', 'Cash on Delivery')], max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mart_admin.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('product_image', models.FileField(upload_to='')),
                ('product_quantity', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mart_admin.Category')),
            ],
        ),
    ]
