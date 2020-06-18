from rest_framework import serializers
<<<<<<< HEAD
from .models import Member
=======
from .models import MemberauthMember,MemberauthMemberCourse, MemberauthSubject
>>>>>>> 595677241dbf7e52d3a13b0312e92363234bae39

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberauthMember
        fields = ['name', 'grade', 'grade_number', 'mac_address', 'department']

# class Member_courseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Member_course
#         fields = ['Member_num','lecture_id']
# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = ['lecture_name', 'lecture_room', 'department', 'lecture_id']
