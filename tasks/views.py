from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from . import models, filter
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from . forms import TaskForm
from task_manager import mixins
from django.contrib.messages.views import SuccessMessageMixin


class TaskCreateView(SuccessMessageMixin, mixins.MyLoginRequired, CreateView):
    model = models.Task
    template_name = 'tasks/task_add.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('The task was successfully created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, mixins.MyLoginRequired, UpdateView):
    model = models.Task
    template_name = 'tasks/task_update.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully changed')


class TaskDeleteView(SuccessMessageMixin, mixins.MyTaskMixin, DeleteView):
    mixin_text = _('You have not permission to delete task')
    model = models.Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task was successfully deleted')


class TaskDetailView(mixins.MyLoginRequired, DetailView):
    model = models.Task
    template_name = 'tasks/task_view.html'
    context_object_name = 'task'


class TaskFilterView(mixins.MyLoginRequired, FilterView):
    filterset_class = filter.TaskFilter
