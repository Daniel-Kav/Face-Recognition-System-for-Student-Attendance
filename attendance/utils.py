import cv2
import os
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



