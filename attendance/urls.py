# attendance/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.capture_and_recognize, name='upload_image'),
]
