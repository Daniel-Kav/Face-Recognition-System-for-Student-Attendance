from django import forms

class UploadImageForm(forms.Form):
    face_image = forms.ImageField()