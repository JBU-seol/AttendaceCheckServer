from django.shortcuts import render
from django.http import HttpResponse, JsonResponse , HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib import messages
from .models import Member, Member_course, Subject, Subject_time, ProMember, ProMember_course
from .serializers import MemberSerializer
from rest_framework.parsers import JSONParser

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
        for course_obj in Member_course.objects.filter(Member_num_id=obj.id):
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
    idd = Member.objects.get(grade_number=student_id)
    id_value = idd.id
    for lec in lec_lists:
        qs = Member_course(Member_num_id = id_value, lecture_id = lec)
        qs.save()
    return render(request, 'students/ResLec.html')
