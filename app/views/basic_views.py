from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import models
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from app.models import Tasks
from app.serializers import TaskSerializer
import psycopg2
import uuid
 
@csrf_exempt

def taskApi(request,id=0):
	if request.method=='GET':
		tasks = Tasks.objects.all()
		task_serializer = TaskSerializer(tasks,many=True)
		return JsonResponse(task_serializer.data, safe=False)

	elif request.method=='POST':
		task_data = JSONParser().parse(request)
		task_serializer = TaskSerializer(data=task_data)
		if task_serializer.is_valid():
			task_serializer.save()
			return JsonResponse("Added Successfully!!", safe=False)
		return JsonResponse("Failed to Add", safe=False)

	elif request.method=='PUT':
		task_data = JSONParser().parse(request)
		task= Tasks.objects.get(task_id=task_data['task_id'])
		task_serializer=TaskSerializer(task,data=task_data)
		if task_serializer.is_valid():
			task_serializer.save()
			return JsonResponse("Added Successfully!!", safe=False)
		return JsonResponse("Failed to Add", safe=False)

	elif request.method =='DELETE':
		task=Tasks.objects.get(task_id=id)
		task.delete()
		return JsonResponse("Deleted Successfully" ,safe=False)

