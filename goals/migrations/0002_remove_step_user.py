# Generated by Django 3.2 on 2021-05-06 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='user',
        ),
    ]