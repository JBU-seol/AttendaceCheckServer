from django.contrib import admin
from .models import Member, Member_course, ProMember, ProMember_course, Subject_time, Subject, logTable,Log

admin.site.register(Member)
admin.site.register(Member_course)
admin.site.register(ProMember_course)
admin.site.register(ProMember)
admin.site.register(Subject)
admin.site.register(Subject_time)
admin.site.register(logTable)
admin.site.register(Log)
