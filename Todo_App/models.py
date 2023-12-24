from django.db import models
from django.contrib.auth.models import AbstractUser , User
# Create your models here.
class User(AbstractUser):
    pass
class Todos(models.Model):
    title = models.CharField( max_length=50)
    details = models.TextField()
    
    def __str__(self):
        return self.title