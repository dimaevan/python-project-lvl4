from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from . import models, filter
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from . forms import TaskForm


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = models.Task
    template_name = 'tasks/task_add.html'
    form_class = TaskForm
    # fields = ['name', 'description', 'workers', 'status', 'label']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = models.Task
    template_name = 'tasks/task_update.html'
    form_class = TaskForm
    # fields = ['name', 'description', 'workers', 'status', 'label']
    success_url = reverse_lazy('tasks')


class TaskDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = models.Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks')

    def test_func(self):
        obj = self.get_object()
        return obj.author.id == self.request.user.id

    def handle_no_permission(self):
        text = _('You have not permission to delete this task')
        messages.add_message(self.request, messages.WARNING, text)
        return redirect('tasks')


class TaskDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.Task
    template_name = 'tasks/task_view.html'
    context_object_name = 'task'


class TaskFilterView(LoginRequiredMixin, FilterView):
    filterset_class = filter.TaskFilter
    login_url = reverse_lazy('login')
