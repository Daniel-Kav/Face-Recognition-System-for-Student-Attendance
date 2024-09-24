# attendance/models.py

from django.db import models
from django.contrib.auth.models import User

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     roll_number = models.CharField(max_length=20, unique=True)
#     profile_image = models.ImageField(upload_to='profile_images')

#     def __str__(self):
#         return self.name

# class Class(models.Model):
#     name = models.CharField(max_length=100)
#     students = models.ManyToManyField(Student, related_name='classes')

#     def __str__(self):
#         return self.name

# class AttendanceRecord(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     present = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.student.name} - {self.date} - {'Present' if self.present else 'Absent'}"

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/images/', blank=True, null=True)

    def __str__(self):
        return self.full_name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.timestamp}"
