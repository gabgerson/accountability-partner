# Generated by Django 3.1.7 on 2021-04-14 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_auto_20210414_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='progress',
            field=models.TextField(default='In Progress'),
        ),
    ]
