from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('parent', 'Parent'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('bus', 'Bus Supervisor'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)