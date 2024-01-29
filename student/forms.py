from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Student

class StudentCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = UserCreationForm.Meta.fields + ('course', 'date_of_birth', 'profile_image')

class StudentAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Student
