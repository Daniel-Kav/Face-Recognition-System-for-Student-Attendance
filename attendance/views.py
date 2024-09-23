
# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
from .utils import capture_student_image

def capture_image(request, student_id):
    student = Student.objects.get(student_id=student_id)
    capture_student_image(student.student_id, student.full_name)
    return redirect('attendance_list')
