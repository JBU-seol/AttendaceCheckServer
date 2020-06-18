# Generated by Django 3.0.2 on 2020-06-14 06:41

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('memberauth', '0039_auto_20200614_1536'),
    ]

    operations = [
        migrations.DeleteModel(
            name='test',
        ),
        migrations.AddField(
            model_name='promember',
            name='department',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='department',
            field=models.CharField(default=datetime.datetime(2020, 6, 14, 6, 41, 52, 423825, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]