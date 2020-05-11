from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Member
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
