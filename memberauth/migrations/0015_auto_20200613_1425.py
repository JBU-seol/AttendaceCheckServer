# Generated by Django 3.0.2 on 2020-06-13 05:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('memberauth', '0014_auto_20200613_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]