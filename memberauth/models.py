from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=20)
    grade = models.CharField(max_length=2)
    grade_number = models.CharField(max_length=10, unique=True)
    mac_address = models.CharField(max_length=20)

    def __str__(self):
        return '%s / %s학년' % (self.name, self.grade)

