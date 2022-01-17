from django.contrib import admin
from .models import Task
from task_manager.models import User

admin.site.register(Task)
admin.site.register(User)
