from django.contrib import admin

from django.contrib import admin
from .models import Course, Student, Instructor

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Instructor)

