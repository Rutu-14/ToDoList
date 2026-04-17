from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    PRIORITY_CHOICES=[
        ('high','High'),
        ('medium','Medium'),
        ('low','Low')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)
    priority=models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    complete=models.BooleanField(default=False)
