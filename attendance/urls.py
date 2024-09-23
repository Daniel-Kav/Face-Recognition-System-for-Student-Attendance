from django.urls import path
from . import views

urlpatterns = [
    path('capture/<str:student_id>/', views.capture_image, name='capture_image'),
    path('train/', views.train_model, name='train_model'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
]