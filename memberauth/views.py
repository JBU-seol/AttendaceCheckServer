from django.shortcuts import render
from django.http import HttpResponse, JsonResponse , HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib import messages
from .models import Member, Member_course, ProMember, ProMember_course, Subject, Subject_time, logTable, Log
from .serializers import MemberSerializer
from rest_framework.parsers import JSONParser
from django.utils import timezone
import datetime

day1 = ["09-07", "09-14", "09-21", "09-28", "10-05", "10-12", "10-19", "10-26", "11-02", "11-09", "11-16", "11-23", "11-30", "12-07", "12-14"]
day2 = ["09-08", "09-15", "09-22", "09-29", "10-06", "10-13", "10-20", "10-27", "11-03", "11-10", "11-17", "11-24", "12-01", "12-08", "12-15"]
day3 = ["09-09", "09-16", "09-23", "09-30", "10-07", "10-14", "10-21", "10-28", "11-04", "11-11", "11-18", "11-25", "12-02", "12-09", "12-16"]
day4 = ["09-10", "09-17", "09-24", "10-01", "10-08", "10-15", "10-22", "10-29", "11-05", "11-12", "11-19", "11-26", "12-03", "12-10", "12-17"]
day5 = ["09-11", "09-18", "09-25", "10-02", "10-09", "10-16", "10-23", "10-30", "11-96", "11-13", "11-20", "11-27", "12-04", "12-11", "12-18"]

@csrf_exempt
def member_list(request):
    if request.method == 'GET':
        query_set = Member.objects.all()
        serializer = MemberSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def course_id_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_grade_number = data['grade_number']
        obj = Member.objects.get(grade_number=search_grade_number)
        data_dict = { "lecture_id":[]}
        for course_obj in Member_course.objects.filter(Member_num_id=obj.id):
            data_dict["lecture_id"].append(course_obj.lecture_id)
        return JsonResponse(data_dict, status=200)

@csrf_exempt
def Procourse_id_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_grade_number = data['grade_number']
        obj = ProMember.objects.get(grade_number=search_grade_number)
        data_dict = { "lecture_id":[]}
        for course_obj in ProMember_course.objects.filter(ProMember_num_id=obj.id):
            data_dict["lecture_id"].append(course_obj.lecture_id)
        return JsonResponse(data_dict, status=200)


@csrf_exempt
def course_name_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_lecture_id = data['lecture_id']
        obj = Subject.objects.get(lecture_id=search_lecture_id)
        data_dict = { "id": obj.id, "lecture_name": obj.lecture_name, "lecture_room": obj.lecture_room,
                      "department": obj.department}
        return JsonResponse(data_dict, status=200)

@csrf_exempt
def course_time_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_id = data['id']
        objs = Subject_time.objects.filter(Subject_num_id = search_id)
        objs_dict = { search_id: []}
        for obj in objs:
            data_dict = { "id": search_id, "year": obj.year, "day": obj.day, "which_day": obj.which_day,
                          "start_time": obj.start_time, "finish_time": obj.finish_time}
            objs_dict[search_id].append(data_dict)
        return JsonResponse(objs_dict, status=200)

@csrf_exempt
def studentList(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_lec = data['lecture_name']
        getObj = Subject.objects.get( lecture_name = search_lec )
        lec_id = getObj.lecture_id
        #print( "lec_id : " + lec_id)
        objs = Member_course.objects.filter( lecture_id = lec_id)
        data_dict = { "students" : []}
        for obj in objs:
            #print( obj.Member_num_id)
            member = Member.objects.get( id = obj.Member_num_id)
            #print( member.name)
            data_dict["students"].append( {"name" : member.name,"grade_number": member.grade_number })
        return JsonResponse(data_dict, status=200)
    else:
        return HttpResponse(status=400)



@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_grade_number = data['grade_number']
        obj = Member.objects.get(grade_number=search_grade_number)
        dictName = {"name": obj.name}
        if data['mac_address'] == obj.mac_address:
            return JsonResponse( dictName,status=200)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)

def regStudent(request):
    return render(request, 'students/registerStudent.html')

def regConStudent(request):
    name = request.POST['name']
    grade = request.POST['grade']
    student_id = request.POST['student_id']
    mac_addr = request.POST['mac_addr']
    department = request.POST['department']
    subjects = Subject.objects.all()
    context = { 'subjects':subjects, 'student_id': student_id, 'name':name}
    try:
        qs = Member(name=name, grade=grade, grade_number=student_id, mac_address=mac_addr, department=department)
        qs.save()
        return render(request, 'students/response.html', context)
    except IntegrityError:
        messages.info(request, '등록된 학번이 있습니다.')
        return HttpResponseRedirect('/')

def regLec(request):
    lec_lists = request.POST.getlist('lecinfo[]')
    student_id = request.POST['student_id']
    obj = Member.objects.get(grade_number=student_id)
    id_value = obj.id
    mac_value = obj.mac_address
    for lec in lec_lists:
        qs1 = Member_course(Member_num_id = id_value, lecture_id = lec)
        qs2 = logTable(macAddress = mac_value, gradeNumber=student_id, lecture_id=lec)
        qs1.save()
        qs2.save()
    return render(request, 'students/ResLec.html')



@csrf_exempt
def attendanceList(request):
    data = JSONParser().parse(request)
    grade_number = data['grade_number']
    lecture_name = data['lecture_name']
    lecObj = Subject.objects.get(lecture_name = lecture_name)
    memObj = Member.objects.get(grade_number=grade_number)
    lecture_id = lecObj.lecture_id
    mac_address = memObj.mac_address
    logObj = logTable.objects.get(macAddress=mac_address, gradeNumber=grade_number, lecture_id=lecture_id)
    dic = { 'week' : []}
    dic['week'].append(logObj.one_week)
    dic['week'].append(logObj.two_week)
    dic['week'].append(logObj.three_week)
    dic['week'].append(logObj.four_week)
    dic['week'].append(logObj.five_week)
    dic['week'].append(logObj.six_week)
    dic['week'].append(logObj.seven_week)
    dic['week'].append(logObj.eight_week)
    dic['week'].append(logObj.nine_week)
    dic['week'].append(logObj.ten_week)
    dic['week'].append(logObj.eleven_week)
    dic['week'].append(logObj.twelve_week)
    dic['week'].append(logObj.thirteen_week)
    dic['week'].append(logObj.fourteen_week)
    dic['week'].append(logObj.fifteen_week)
    dic['week'].append(logObj.sixteen_week)

    return JsonResponse( dic, status=200)

@csrf_exempt
def logtest(request):
    data = JSONParser().parse(request)
    grade_number = data['grade_number']
    lecture_name = data['lecture_name']
    lecObj = Subject.objects.get(lecture_name=lecture_name)
    memObj = Member.objects.get(grade_number=grade_number)
    lecture_id = lecObj.lecture_id
    lecture_room = lecObj.lecture_room
    mac_address = memObj.mac_address
    subject_num_id = lecObj.id
    timeObj = Subject_time.objects.get(Subject_num_id = subject_num_id)

    #array 선택
    if timeObj.day=='09-07':
        arrayDay = day1
    elif timeObj.day=='09-08':
        arrayDay = day2
    elif timeObj.day=='09-09':
        arrayDay = day3
    elif timeObj.day=='09-10':
        arrayDay = day4
    elif timeObj.day=='09-11':
        arrayDay = day5

    #index 선택
    now = datetime.datetime.now()
    if datetime.datetime(2020,9,7)<now<datetime.datetime(2020,9,14):#14->12수정해야함.
        i = 0
    elif datetime.datetime(2020,9,14)<now<datetime.datetime(2020,9,19):
        i = 1
    elif datetime.datetime(2020, 9, 21) < now < datetime.datetime(2020, 9, 26):
        i = 2
    elif datetime.datetime(2020, 9, 28) < now < datetime.datetime(2020, 10, 3):
        i = 3
    elif datetime.datetime(2020, 10, 5) < now < datetime.datetime(2020, 10, 10):
        i = 4
    elif datetime.datetime(2020, 10, 12) < now < datetime.datetime(2020, 10, 17):
        i = 5
    elif datetime.datetime(2020, 10, 19) < now < datetime.datetime(2020, 10, 24):
        i = 6
    elif datetime.datetime(2020, 10, 26) < now < datetime.datetime(2020, 10, 31):
        i = 7
    elif datetime.datetime(2020, 11, 2) < now < datetime.datetime(2020, 11, 7):
        i = 8
    elif datetime.datetime(2020, 11, 9) < now < datetime.datetime(2020, 11, 14):
        i = 9
    elif datetime.datetime(2020, 11, 16) < now < datetime.datetime(2020, 11, 21):
        i = 10
    elif datetime.datetime(2020, 11, 23) < now < datetime.datetime(2020, 11, 28):
        i = 11
    elif datetime.datetime(2020, 11, 30) < now < datetime.datetime(2020, 12, 5):
        i = 12
    elif datetime.datetime(2020, 12, 7) < now < datetime.datetime(2020, 12, 12):
        i = 13
    elif datetime.datetime(2020, 12, 14) < now < datetime.datetime(2020, 12, 19):
        i = 14

    timeSentence1 = timeObj.year + "-" + arrayDay[i] + " " + timeObj.start_time + ":00.000000+00:00"
    timeSentence2 = timeObj.year + "-" + arrayDay[i] + " " + timeObj.finish_time + ":00.000000+00:00"


    #logObjs = Log.objects.filter(mac_addr=mac_address, lecture_room=lecture_room,
    #                             time__range=[timeSentence1, timeSentence2])
    logObjs_count = Log.objects.filter(mac_addr=mac_address, lecture_room=lecture_room,
                                 time__range=[timeSentence1, timeSentence2]).count()
    print(logObjs_count)
    logtableObj = logTable.objects.get(macAddress=mac_address, lecture_id=lecture_id)
    print(logtableObj.id)
    #출결여부 결정
    if logObjs_count>8:#출석체크 강도 설정
        value=1#출석
    elif logObjs_count>3:
        value=2#지각
    else:
        value=0#결석
    #주차정보 셋팅
    if i == 0:
        logtableObj.one_week = value
    elif i == 1:
        logtableObj.two_week = value
    elif i == 2:
        logtableObj.three_week = value
    elif i == 3:
        logtableObj.four_week = value
    elif i == 4:
        logtableObj.five_week = value
    elif i == 5:
        logtableObj.six_week = value
    elif i == 6:
        logtableObj.seven_week = value
    elif i == 7:
        logtableObj.eight_week = value
    elif i == 8:
        logtableObj.nine_week = value
    elif i == 9:
        logtableObj.ten_week = value
    elif i == 10:
        logtableObj.eleven_week = value
    elif i == 11:
        logtableObj.twelve_week = value
    elif i == 12:
        logtableObj.thirteen_week = value
    elif i == 13:
        logtableObj.fourteen_week = value
    elif i == 14:
        logtableObj.fifteen_week = value
    logtableObj.save()

    return HttpResponse(status=200)

# next_day = now + datetime.timedelta(days=7)
