from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	course_name = models.CharField(max_length = 50)
	course_type = models.CharField(max_length = 15)
	course_discription = models.TextField()
	course_website = models.URLField()

class Student(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	student_password = models.CharField(max_length = 20)
	student_ID = models.CharField(max_length = 15)
	date_of_birth = models.DateTimeField()
	student_email = models.EmailField(blank = True)
	current_year = models.DateTimeField();
	current_courses = models.ManyToManyField(Course)
	def __str__(self):
		return u'%s %s' %(self.first_name, self.last_name)

class Faculty(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	faculty_password = models.CharField(max_length = 20)
	department = models.CharField(max_length =50)
	faculty_email = models.EmailField(blank = True)
	extension = models.CharField(max_length= 15, null = True, blank = True)
	research_area = models.TextField(null = True)
	Result = models.ManyToManyField(Course)

class PlacementDrive(models.Model):
	company_name = models.CharField(max_length = 30)
	company_detail = models.TextField()
	company_technology = models.TextField()
	company_salary = models.IntegerField()
	company_contacts = models.TextField()
	related_faculty = models.ForeignKey(Faculty)


class DiscussionForum(models.Model):
	forum_name = models.CharField(max_length = 30)
	forum_created = models.DateTimeField()
	forum_update = models.DateTimeField(auto_now = True)
	forum_student_ID = models.ManyToManyField(Student)
	forum_faculty_ID  = models.ManyToManyField(Faculty)

class ExamSchedule(models.Model):
	category_choices = (
    	('QZ', 'Quiz'),
    	('MS', 'Mid Semester'),
    	('ES', 'End Semester'),
    	('AS', 'Assignment'),
	) 
	exam_date = models.DateTimeField()
	exam_details = models.TextField()
	exam_courses = models.ManyToManyField(Course)
	exam_students = models.ManyToManyField(Student)
	exam_category = models.CharField(max_length = 3, choices = category_choices)

class Result(models.Model):
	result_document =  models.FileField(upload_to='result_docs/%Y/%m/%d/')
	result_details = models.ForeignKey(Course, on_delete = models.CASCADE)