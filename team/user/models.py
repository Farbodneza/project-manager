from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=14)
    class Meta:
        permissions = [
            ("can_start_project", "can start a new project"),
        ]
        
    
    
