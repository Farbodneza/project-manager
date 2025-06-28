from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from team_manager.serializers import TeamSerializer, ProjectSerializer
from team_manager.models import Team, Project
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from user.permissions import IsPtojectMember, CanCreateProject

# Create your views here.


class TeamListViewset(viewsets.GenericViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def list(self, request, *args, **kwargs):
        teams = self.get_queryset()
        serializer = self.get_serializer(teams, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
class TeamDetaialViewset(RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = "pk"
    

class ProjectListViewset(viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [CanCreateProject]
    def list(self, request, *args, **kwargs):
        projects = self.get_queryset()
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    

class ProjectDetailstViewset(RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [IsPtojectMember]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = "pk"

