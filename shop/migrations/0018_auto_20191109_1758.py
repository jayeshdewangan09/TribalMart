# Generated by Django 2.2.4 on 2019-11-09 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20191109_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerquery',
            name='query_id',
            field=models.CharField(default=datetime.datetime(2019, 11, 9, 17, 58, 55, 638686), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default=datetime.datetime(2019, 11, 9, 17, 58, 55, 638686), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='update_id',
            field=models.CharField(default=datetime.datetime(2019, 11, 9, 17, 58, 55, 638686), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 11, 9, 17, 58, 55, 638686), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 11, 9, 17, 58, 55, 638686), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 11, 9, 17, 58, 55, 638686), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='request_id',
            field=models.CharField(default=datetime.datetime(2019, 11, 9, 17, 58, 55, 638686), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pulled_requests',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 11, 9, 17, 58, 55, 638686), max_length=50, primary_key=True, serialize=False),
        ),
    ]