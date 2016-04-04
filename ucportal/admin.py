from django.contrib import admin
from .models import Student, Faculty, Course, DiscussionForum, ExamSchedule

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(DiscussionForum)
admin.site.register(ExamSchedule)