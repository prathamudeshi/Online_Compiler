from django.db import models
from django.contrib.auth.models import User

class CCode(models.Model):
    code = models.TextField()
    output = models.TextField()
    user = models.ForeignKey(User, on_delete =  models.CASCADE, null = True, blank = True)
    tc_pass = models.BooleanField(null = True)
# Create your models here.
    