
# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
from .utils import capture_student_image,recognize_faces_and_mark_attendance,train_face_recognizer


def capture_image(request, student_id):
    student = Student.objects.get(student_id=student_id)
    capture_student_image(student.student_id, student.full_name)
    return redirect('attendance_list')

def train_model(request):
    train_face_recognizer()
    return render(request, 'attendance/train_success.html')

def mark_attendance(request):
    recognize_faces_and_mark_attendance()
    return render(request, 'attendance/attendance_success.html')