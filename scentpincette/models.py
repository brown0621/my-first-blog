from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)


    def __str__(self):
        return self.email
		