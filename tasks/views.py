from django.views.generic import ListView, CreateView, UpdateView
from . import models
from django.urls import reverse_lazy


class TasksListView(ListView):
    template_name = 'tasks/tasks_list.html'
    model = models.Task


class TaskCreateView(CreateView):
    model = models.Task
    template_name = 'tasks/task_add.html'
    fields = ['title', 'text', 'author']
    success_url = reverse_lazy('tasks')


class TaskUpdateView(UpdateView):
    model = models.Task
    template_name = 'tasks/task_update.html'
    fields = ['title', 'text', ]
    success_url = reverse_lazy('tasks')