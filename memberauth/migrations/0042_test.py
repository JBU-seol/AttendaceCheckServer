# Generated by Django 3.0.2 on 2020-06-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberauth', '0041_merge_20200618_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
            ],
        ),
    ]
