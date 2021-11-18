from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Test(models.Model):
    id=models.AutoField(primary_key=True)
    col=models.CharField(max_length=10)