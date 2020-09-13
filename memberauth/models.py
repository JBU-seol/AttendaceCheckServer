from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=20)
    grade = models.CharField(max_length=2)
    grade_number = models.CharField(max_length=10, unique=True)
    mac_address = models.CharField(max_length=20)
    department = models.CharField(max_length=20, default='기타')

    def __str__(self):
        return '%s - %s학년 / %s' % (self.department, self.grade, self.name)

class Member_course(models.Model):
    Member_num = models.ForeignKey(Member,on_delete=models.CASCADE)
    lecture_id = models.CharField(max_length=8)

    def __str__(self):
        return '%s - %s' %(self.Member_num, self.lecture_id)

class ProMember(models.Model):
    name = models.CharField(max_length=20)
    grade_number = models.CharField(max_length=10, unique=True)
    mac_address = models.CharField(max_length=20)
    department = models.CharField(max_length=20, default='기타')

    def __str__(self):
        return '%s / %s' % ( self.name, self.department )

class ProMember_course(models.Model):
    ProMember_num = models.ForeignKey(ProMember,on_delete=models.CASCADE)
    lecture_id = models.CharField(max_length=8)

    def __str__(self):
        return '%s - %s' %(self.ProMember_num, self.lecture_id)

class Subject(models.Model):
    lecture_name = models.CharField(max_length=30)
    lecture_room = models.CharField(max_length=7)
    department = models.CharField(max_length=20)
    lecture_id = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.lecture_name

class Subject_time(models.Model):
    Subject_num = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.CharField(max_length=5)
    day = models.CharField(max_length=10)
    which_day = models.CharField(max_length=8)
    start_time = models.CharField(max_length=8)
    finish_time = models.CharField(max_length=8)

    def __str__(self):
        return '%s - %s - %s' %( self.Subject_num, self.start_time, self.finish_time)

class logTable(models.Model):
    macAddress = models.CharField(max_length=20)
    gradeNumber = models.CharField(max_length=15)
    lecture_id = models.CharField(max_length=8)
    one_week = models.IntegerField(default=1)
    two_week = models.IntegerField(default=1)
    three_week = models.IntegerField(default=1)
    four_week = models.IntegerField(default=1)
    five_week = models.IntegerField(default=1)
    six_week = models.IntegerField(default=1)
    seven_week = models.IntegerField(default=1)
    eight_week = models.IntegerField(default=1)
    nine_week =models.IntegerField(default=1)
    ten_week = models.IntegerField(default=1)
    eleven_week = models.IntegerField(default=1)
    twelve_week = models.IntegerField(default=1)
    thirteen_week = models.IntegerField(default=1)
    fourteen_week = models.IntegerField(default=1)
    fifteen_week = models.IntegerField(default=1)
    sixteen_week = models.IntegerField(default=1)

    def __str__(self):
        return '%s / %s / %s' %(self.macAddress, self.gradeNumber, self.lecture_id)
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Log(models.Model):
    num = models.AutoField(primary_key=True)
    mac_addr = models.CharField(max_length=20)
    lecture_room = models.CharField(max_length=7)
    pwr = models.IntegerField()
    count = models.IntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Log'

