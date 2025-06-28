from rest_framework.permissions import BasePermission, SAFE_METHODS
from team_manager.models import Project, Team
from task_manager.models import Task


class IsPtojectMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user in obj.team.users.all()

class CanCreateTask(BasePermission):
    def has_permission(self, request, view):
        if request.method is "POST":
            project_id = request.data.get("project_id")
            if not project_id:
                return False
            project = Project.objects.get(id=project_id)
            return request.user in project.team_project.users.all()
        return True
    

class IsTaskOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        task_user = obj.user
        return request.user == task_user
    

class CanCreateProject(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('user.can_start_project')

        
    # {
#     "username": "farbod",
#     "password": "1"
# }
