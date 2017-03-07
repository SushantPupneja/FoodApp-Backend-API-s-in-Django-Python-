# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppUsers', '0004_auto_20170217_0115'),
        ('orders', '0002_auto_20170305_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_order_receipt_no', models.CharField(default='Test', max_length=30)),
                ('entity', models.CharField(default='Payment', max_length=10)),
                ('amount', models.IntegerField()),
                ('currency', models.CharField(default='INR', max_length=20)),
                ('status', models.CharField(choices=[('created', 'created'), ('authorized', 'authorized'), ('captured', 'captured'), ('refunded', 'refunded'), ('failed', 'failed')], default='created', max_length=20)),
                ('method', models.CharField(choices=[('card', 'card'), ('netbanking', 'netbanking'), ('wallet', 'wallet'), ('emi', 'emi')], default='Card', max_length=20)),
                ('description', models.CharField(default='None', max_length=100)),
                ('international', models.BooleanField(default=False)),
                ('refund_status', models.CharField(choices=[('null', 'null'), ('partial', 'partial'), ('full', 'full')], default='null', max_length=20)),
                ('amount_refunded', models.IntegerField(default=0)),
                ('captured', models.BooleanField(default=False)),
                ('fee', models.IntegerField(default=0)),
                ('service_tax', models.IntegerField(default=0)),
                ('error_code', models.CharField(default='None', max_length=20)),
                ('error_description', models.CharField(default='None', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppUsers.AppUser')),
            ],
        ),
    ]