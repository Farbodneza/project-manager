from django.contrib import admin
from user.models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('username', 'pk')
    search_fields = ('username',)
