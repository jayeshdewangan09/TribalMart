# Generated by Django 2.2.4 on 2019-10-02 04:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190925_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.CharField(default=datetime.datetime(2019, 10, 2, 10, 16, 55, 811026), max_length=50, primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('cust_name', models.CharField(max_length=80)),
                ('cust_email', models.EmailField(max_length=254)),
                ('address1', models.CharField(default='', max_length=200)),
                ('address2', models.CharField(default='', max_length=200)),
                ('address3', models.CharField(default='', max_length=200)),
                ('town_city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('address_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='customerquery',
            name='query_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 10, 16, 55, 811026), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 10, 16, 55, 810027), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 10, 16, 55, 810027), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 10, 16, 55, 810027), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='request_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 10, 16, 55, 810027), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pulled_requests',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 10, 16, 55, 810027), max_length=50, primary_key=True, serialize=False),
        ),
    ]