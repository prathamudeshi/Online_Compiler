from django.db import models
from django.contrib.auth.models import User
from pycompiler.models import *

class Student(models.Model):
    rollno = models.IntegerField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    qs_solved = models.ManyToManyField('Questions', blank=True)

class Faculty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Questions(models.Model):
    qs_title = models.CharField(max_length = 100, null = True)
    qs_id = models.IntegerField(unique=True, primary_key=True)
    stu = models.ManyToManyField(User, blank=True)
    question = models.TextField()

class TestCase(models.Model):
    qs_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    testcase_input = models.TextField()
    expected_output = models.TextField()
