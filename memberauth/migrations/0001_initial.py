# Generated by Django 3.0.2 on 2020-06-18 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=2)),
                ('grade_number', models.CharField(max_length=10, unique=True)),
                ('mac_address', models.CharField(max_length=20)),
                ('department', models.CharField(default='기타', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('grade_number', models.CharField(max_length=10, unique=True)),
                ('mac_address', models.CharField(max_length=20)),
                ('department', models.CharField(default='기타', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_name', models.CharField(max_length=30)),
                ('lecture_room', models.CharField(max_length=7)),
                ('department', models.CharField(max_length=20)),
                ('lecture_id', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=5)),
                ('day', models.CharField(max_length=10)),
                ('which_day', models.CharField(max_length=8)),
                ('start_time', models.CharField(max_length=8)),
                ('finish_time', models.CharField(max_length=8)),
                ('Subject_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memberauth.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='ProMember_course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_id', models.CharField(max_length=8)),
                ('ProMember_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memberauth.ProMember')),
            ],
        ),
        migrations.CreateModel(
            name='Member_course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_id', models.CharField(max_length=8)),
                ('Member_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memberauth.Member')),
            ],
        ),
    ]
