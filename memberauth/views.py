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
    timeSentence = timeObj.year+'-'+timeObj.day+' '+timeObj.start_time+":00.000000+00:00"


    logObjs = Log.objects.filter(mac_addr=mac_address, lecture_room=lecture_room,
                                 time__range=['2020-06-01 12:00:00.000000+00:00', timeSentence])
    print(logObjs)


    return HttpResponse(status=200)


# next_day = now + datetime.timedelta(days=7)