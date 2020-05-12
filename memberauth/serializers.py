from rest_framework import serializers
from .models import Member,Member_course

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['name', 'grade', 'grade_number', 'mac_address', 'department']

class Member_courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member_course
        fields = ['Member_num','lecture_id']

