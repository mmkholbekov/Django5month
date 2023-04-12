from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ConfirmUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
