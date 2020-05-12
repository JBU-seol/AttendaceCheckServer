from django.contrib import admin
from .models import Member, Member_course,Subject, Subject_time

admin.site.register(Member)
admin.site.register(Member_course)
admin.site.register(Subject)
admin.site.register(Subject_time)
