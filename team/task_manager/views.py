from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from task_manager.serializers import TaskSerializer
from task_manager.models import Task
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from user.permissions import IsTaskOwner, CanCreateTask



class TaskListViewset(viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [CanCreateTask]
    def list(self, request, *args, **kwargs):
        tasks = self.get_queryset()
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
class TaskDetaialViewset(RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes= [IsTaskOwner]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = "pk"


# {
#     "username": "farbod",
#     "password": "1"
# }