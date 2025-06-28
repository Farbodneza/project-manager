from django.db import models
from user.models import CustomUser
# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(CustomUser, related_name='user_team')
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, related_name='team_project', on_delete=models.CASCADE)
    class Meta:
        permissions = [
            ("can_create_project", "Can start a new project"),
        ]
