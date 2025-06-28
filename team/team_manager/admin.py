from django.contrib import admin
from team_manager.models import Team, Project
# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')
    search_fields = ('name',)
