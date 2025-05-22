# Face Recognition System for Student Attendance

## Description

This project is a web-based student attendance system that uses face recognition to mark attendance. It's built using Django and leverages libraries like OpenCV and dlib for face detection and recognition.

## Features

- Student registration with image capture.
- Training of a face recognition model based on captured student images.
- Automated attendance marking by recognizing faces from a live camera feed.
- Records attendance with timestamps.

## Technologies Used

- Django
- OpenCV
- dlib
- face-recognition
- numpy
- scikit-learn
- scipy
- Pillow
- Other dependencies listed in `requirements.txt`

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd Face-Recognition-System-for-Student-Attendance
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    pip install dlib-19.24.1-cp311-cp311-win_amd64.whl  # Install the provided dlib wheel file
    ```

4.  **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional, for accessing Django admin):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application should now be running at `http://127.0.0.1:8000/`.

## How to Use

1.  **Register Students:** Add student details through the Django admin or a dedicated registration interface (if available).

2.  **Capture Student Images:** Navigate to the image capture view (as seen in `attendance/views.py`) to capture images for each student. Ensure you capture multiple images of each student for better recognition accuracy.

3.  **Train the Face Recognizer:** Access the view or management command that triggers the `train_face_recognizer` function (as seen in `attendance/views.py`). This will train the model using the captured images.

4.  **Mark Attendance:** Go to the attendance marking view. The system will use the camera feed to detect and recognize faces, marking attendance for recognized students.

## Project Structure

```
.
├── attendance_sys/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── attendance/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   └── attendance/
│   │       └── train_success.html
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── media/
├── db.sqlite3
├── dlib-19.24.1-cp311-cp311-win_amd64.whl
├── manage.py
└── requirements.txt
``` 