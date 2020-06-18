# Generated by Django 3.0.2 on 2020-06-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberauth', '0036_delete_logtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='logTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('macAddress', models.CharField(max_length=10)),
                ('gradeNumber', models.CharField(max_length=15)),
                ('lecture_id', models.CharField(max_length=8)),
                ('one_week', models.BooleanField(default=0)),
                ('two_week', models.BooleanField(default=0)),
                ('three_week', models.BooleanField(default=0)),
                ('four_week', models.BooleanField(default=0)),
                ('five_week', models.BooleanField(default=0)),
                ('six_week', models.BooleanField(default=0)),
                ('seven_week', models.BooleanField(default=0)),
                ('eight_week', models.BooleanField(default=0)),
                ('nine_week', models.BooleanField(default=0)),
                ('ten_week', models.BooleanField(default=0)),
                ('eleven_week', models.BooleanField(default=0)),
                ('twelve_week', models.BooleanField(default=0)),
                ('thirteen_week', models.BooleanField(default=0)),
                ('fourteen_week', models.BooleanField(default=0)),
                ('fifteen_week', models.BooleanField(default=0)),
                ('sixteen_week', models.BooleanField(default=0)),
            ],
        ),
    ]