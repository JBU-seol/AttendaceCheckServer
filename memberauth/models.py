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
    macAddress = models.CharField(max_length=10)
    gradeNumber = models.CharField(max_length=15)
    lecture_id = models.CharField(max_length=8)
    one_week = models.BooleanField(default=0)
    two_week = models.BooleanField(default=0)
    three_week = models.BooleanField(default=0)
    four_week = models.BooleanField(default=0)
    five_week = models.BooleanField(default=0)
    six_week = models.BooleanField(default=0)
    seven_week = models.BooleanField(default=0)
    eight_week = models.BooleanField(default=0)
    nine_week =models.BooleanField(default=0)
    ten_week = models.BooleanField(default=0)
    eleven_week = models.BooleanField(default=0)
    twelve_week = models.BooleanField(default=0)
    thirteen_week = models.BooleanField(default=0)
    fourteen_week = models.BooleanField(default=0)
    fifteen_week = models.BooleanField(default=0)
    sixteen_week = models.BooleanField(default=0)

    def __str__(self):
        return '%s / %s / %s' %(self.macAddress, self.gradeNumber, self.lecture_id)

