from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default=True)

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)