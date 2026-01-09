from django.db import models
from users.models import User

class Student(models.Model):
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=50)
    image = models.ImageField(upload_to='students/', null=True, blank=True)
    parents = models.ManyToManyField(User, related_name='children')