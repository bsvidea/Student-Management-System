from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):
    # Add your custom fields here
    course=models.CharField(max_length=25)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

