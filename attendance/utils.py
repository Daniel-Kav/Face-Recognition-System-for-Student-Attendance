import cv2
import os
import numpy as np
from django.conf import settings

def capture_student_image(student_id, full_name):
    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    student_folder = os.path.join(settings.MEDIA_ROOT, f'students/{student_id}_{full_name}')
    if not os.path.exists(student_folder):
        os.makedirs(student_folder)
    
    count = 0
    while count < 20:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            img_name = f"{student_folder}/{student_id}_{count}.jpg"
            cv2.imwrite(img_name, face)
            count += 1
            print(f"{img_name} saved!")
        
        cv2.imshow("Capture Student Image", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cam.release()
    cv2.destroyAllWindows()




def train_face_recognizer(data_dir='students'):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    faces = []
    labels = []
    label_map = {}
    current_label = 0

    for student_folder in os.listdir(data_dir):
        folder_path = os.path.join(data_dir, student_folder)
        if not os.path.isdir(folder_path):
            continue
        
        label_map[current_label] = student_folder
        for img_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            faces.append(img)
            labels.append(current_label)
        
        current_label += 1
    
    recognizer.train(faces, np.array(labels))
    recognizer.write('face_recognizer.yml')

    return label_map

from .models import Student, Attendance
from datetime import datetime

def recognize_faces_and_mark_attendance(label_map, recognizer_model='face_recognizer.yml'):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(recognizer_model)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(face)
            if confidence < 100:
                student_name = label_map[label]
                student_id = student_name.split('_')[0]
                student = Student.objects.get(student_id=student_id)
                
                if not Attendance.objects.filter(student=student, timestamp__date=datetime.now().date()).exists():
                    Attendance.objects.create(student=student)
                    print(f"Attendance marked for {student.full_name}")
            else:
                print("Unknown face detected.")
        
        cv2.imshow("Attendance System", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
