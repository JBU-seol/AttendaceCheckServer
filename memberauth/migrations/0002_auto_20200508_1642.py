# Generated by Django 3.0.2 on 2020-05-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='grade_number',
            field=models.CharField(max_length=10),
        ),
    ]
