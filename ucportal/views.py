from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from django.db import models
import datetime
def index(request):
	context = {'title': 'Welcome to University Portal'}
	return render(request, 'ucportal/facebook.html',context)

def exam(request):
	exam_date_1 = datetime.now()
	exam_instance = ExamSchedule(exam_date= exam_date_1, exam_category = 'QZ')
	return HttpResponse(exam_instance)

