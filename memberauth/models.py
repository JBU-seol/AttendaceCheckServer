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
    mac_addr = models.CharField(max_length=12)
    lecture_room = models.CharField(max_length=7)
    pwr = models.IntegerField()
    count = models.IntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Log'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MemberauthLogtable(models.Model):
    macaddress = models.CharField(db_column='macAddress', max_length=10)  # Field name made lowercase.
    gradenumber = models.CharField(db_column='gradeNumber', max_length=15)  # Field name made lowercase.
    lecture_id = models.CharField(max_length=8)
    one_week = models.IntegerField()
    two_week = models.IntegerField()
    three_week = models.IntegerField()
    four_week = models.IntegerField()
    five_week = models.IntegerField()
    six_week = models.IntegerField()
    seven_week = models.IntegerField()
    eight_week = models.IntegerField()
    nine_week = models.IntegerField()
    ten_week = models.IntegerField()
    eleven_week = models.IntegerField()
    twelve_week = models.IntegerField()
    thirteen_week = models.IntegerField()
    fourteen_week = models.IntegerField()
    fifteen_week = models.IntegerField()
    sixteen_week = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'memberauth_logtable'


class MemberauthMember(models.Model):
    name = models.CharField(max_length=20)
    grade = models.CharField(max_length=2)
    grade_number = models.CharField(unique=True, max_length=10)
    mac_address = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'memberauth_member'


class MemberauthMemberCourse(models.Model):
    lecture_id = models.CharField(max_length=8)
    member_num = models.ForeignKey(MemberauthMember, models.DO_NOTHING, db_column='Member_num_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberauth_member_course'


class MemberauthPromember(models.Model):
    name = models.CharField(max_length=20)
    grade_number = models.CharField(unique=True, max_length=10)
    mac_address = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'memberauth_promember'


class MemberauthPromemberCourse(models.Model):
    lecture_id = models.CharField(max_length=8)
    promember_num = models.ForeignKey(MemberauthPromember, models.DO_NOTHING, db_column='ProMember_num_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberauth_promember_course'


class MemberauthSubject(models.Model):
    lecture_name = models.CharField(max_length=30)
    lecture_room = models.CharField(max_length=7)
    lecture_id = models.CharField(unique=True, max_length=8)

    class Meta:
        managed = False
        db_table = 'memberauth_subject'


class MemberauthSubjectTime(models.Model):
    year = models.CharField(max_length=5)
    day = models.CharField(max_length=10)
    which_day = models.CharField(max_length=8)
    start_time = models.CharField(max_length=8)
    finish_time = models.CharField(max_length=8)
<<<<<<< HEAD

    def __str__(self):
        return '%s - %s - %s' %( self.Subject_num, self.start_time, self.finish_time)

class logTable(models.Model):
    macAddress = models.CharField(max_length=20)
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
=======
    subject_num = models.ForeignKey(MemberauthSubject, models.DO_NOTHING, db_column='Subject_num_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberauth_subject_time'
>>>>>>> 595677241dbf7e52d3a13b0312e92363234bae39
