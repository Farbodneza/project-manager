from django.db import models
from team_manager.models import Project
from user.models import CustomUser


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not_started'),
        ('in_progress', 'In_progress'),
        ('in_review', 'In_review'),
        ('in_test', 'In_Test'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Not_started'
    )
    dead_line = models.DateField()
    # int choice
    # use choices for priority
    Priority = models.CharField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='user_task', on_delete=models.CASCADE)


# class IsAdmin(KatebBasePermission):
#     message = _("You must be the Admin to call this")

#     def has_permission(self, request, view):
#         is_auth = request.user and request.user.is_authenticated
#         if V2_PERMISSIONS:
#             is_admin = self.belongs_to_role_type(request, Role.Type.ADMIN)
#         else:
#             is_admin = request.user.groups.filter(name="admin").exists()

#         return is_auth and is_admin

#     def has_object_permission(self, request, view, obj):
#         return