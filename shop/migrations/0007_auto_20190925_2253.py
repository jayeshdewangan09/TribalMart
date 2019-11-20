# Generated by Django 2.2.4 on 2019-09-25 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190910_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerQuery',
            fields=[
                ('query_id', models.CharField(default=datetime.datetime(2019, 9, 25, 22, 53, 12, 22521), max_length=50, primary_key=True, serialize=False)),
                ('cust_email', models.EmailField(max_length=254)),
                ('query', models.CharField(max_length=1000)),
                ('query_date', models.CharField(max_length=50)),
                ('query_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 9, 25, 22, 53, 12, 22521), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 9, 25, 22, 53, 12, 22521), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 9, 25, 22, 53, 12, 22521), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='request_id',
            field=models.CharField(default=datetime.datetime(2019, 9, 25, 22, 53, 12, 22521), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pulled_requests',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 9, 25, 22, 53, 12, 22521), max_length=50, primary_key=True, serialize=False),
        ),
    ]