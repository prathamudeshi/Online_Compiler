from django.db import models
from django.contrib.auth.models import User

class Code(models.Model):
    code = models.TextField()
    output = models.TextField()
    user = models.ForeignKey(User, on_delete =  models.CASCADE, null = True, blank = True)
    tc_pass = models.BooleanField(null = True)
    qs_id = models.IntegerField(null = True)
# Create your models here.
    
