# Generated by Django 3.2 on 2021-05-12 21:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 12, 21, 59, 34, 110849, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='step',
            name='deadline',
            field=models.DateTimeField(default=None),
        ),
    ]