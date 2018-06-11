from django.conf import settings
from django.db import models

# Create your models here.
from django.utils import timezone


class School(models.Model):
    school_name = models.CharField(max_length=50)
    school_description = models.CharField(max_length=200)

class Student(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)