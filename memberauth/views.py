from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Member, Member_course, Subject, Subject_time
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
            data_dict = { "year": obj.year, "day": obj.day, "which_day": obj.which_day,
                          "start_time": obj.start_time, "finish_time": obj.finish_time}
            objs_dict[search_id].append(data_dict)
        return JsonResponse(objs_dict, status=200)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_grade_number = data['grade_number']
        obj = Member.objects.get(grade_number=search_grade_number)

        if data['mac_address'] == obj.mac_address:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)
