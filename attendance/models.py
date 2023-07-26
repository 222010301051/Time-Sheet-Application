from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employees(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    #description = models.TextField()
    class Meta:
        db_table = "employees"
    def __str__(self):
        return self.firstname

class Attendance(models.Model):
    name = models.CharField(max_length=200,default='')
    date = models.DateField()
    shift = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    login_time = models.IntegerField()

    def __str__(self):
        return str(self.date)