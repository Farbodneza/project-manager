from django.contrib import admin
from task_manager.models import Task
# Register your models here.

@admin.register(Task)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    search_fields = ('title',)
