# Generated by Django 3.0.2 on 2020-06-14 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberauth', '0033_auto_20200614_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='department',
            field=models.CharField(default='정보보호학과', max_length=20),
        ),
    ]