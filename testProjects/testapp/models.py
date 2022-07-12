from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(auto_created=True, primary_key=True)
    date_of_birth = models.DateField()

class ToDo(models.Model):
    CHOICES = [
        ("L", "Low"),
        ("M", "MEDIUM"),
        ("H", "HIGH")
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)   #user orresponding todo list will be deleted with user
    priority = models.CharField(max_length=1, choices=CHOICES)