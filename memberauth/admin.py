from django.contrib import admin
from .models import Member, Member_course,Subject, Subject_time, ProMember_course, ProMember

admin.site.register(Member)
admin.site.register(Member_course)
admin.site.register(ProMember)
admin.site.register(ProMember_course)
admin.site.register(Subject)
admin.site.register(Subject_time)