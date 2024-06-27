from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Student, Instructor
from .forms import CourseForm, StudentForm, InstructorForm

# Course views
# EduManage/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm

def course_list(request):
    courses = [
        {'name': 'Computer Science'},
        {'name': 'Software Engineering'},
        {'name': 'Business Administration'}
    ]
    return render(request, 'app2/course_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'app2/course_form.html', {'form': form})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'app2/course_form.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'app2/course_confirm_delete.html', {'course': course})


# Similar views for Student and Instructor would be created here

