from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task', 'is_completed', 'updated_at']
    search_fields = ['task']