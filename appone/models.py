from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    note_title=models.CharField(max_length=50)
    note_description=models.CharField(max_length=500)
