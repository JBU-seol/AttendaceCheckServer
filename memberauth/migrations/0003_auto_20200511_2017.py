# Generated by Django 3.0.2 on 2020-05-11 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberauth', '0002_auto_20200508_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={},
        ),
        migrations.RemoveField(
            model_name='member',
            name='created',
        ),
    ]
