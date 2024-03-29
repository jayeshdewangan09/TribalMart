# Generated by Django 2.2.4 on 2019-10-02 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20191002_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='cust_phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='customerquery',
            name='query_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 18, 13, 3, 930006), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 18, 13, 3, 930006), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 18, 13, 3, 928052), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 18, 13, 3, 928052), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 18, 13, 3, 929051), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='request_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 18, 13, 3, 929051), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pulled_requests',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 18, 13, 3, 929051), max_length=50, primary_key=True, serialize=False),
        ),
    ]
