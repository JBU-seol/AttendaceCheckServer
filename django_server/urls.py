"""django_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from memberauth import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', views.member_list),
    path('members/course_id', views.course_id_list),
    path('members/pro_course_id', views.Procourse_id_list),
    path('members/course_name', views.course_name_list),
    path('members/course_time', views.course_time_list),
    path('members/student_list', views.studentList),
    path('members/week_list', views.attendanceList),
    path('members/check', views.logtest),
    path('members/attendance_list', views.get_student_attendance),
    path('members/change_attendance_list', views.change_student_attendance),
    path('login/', views.login),
    path('', views.regStudent, name='reg'),
    path('regCon', views.regConStudent, name='regCon'),
    path('regLec', views.regLec, name='regLec'),
    url(r'^api-auth/', include('rest_framework.urls'))
]
