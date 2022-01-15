from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from . import models, filter
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from . forms import TaskForm
from task_manager import mixins


class TaskCreateView(mixins.MyLoginRequired, CreateView):
    model = models.Task
    template_name = 'tasks/task_add.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(mixins.MyLoginRequired, UpdateView):
    model = models.Task
    template_name = 'tasks/task_update.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')


class TaskDeleteView(mixins.MyTaskMixin, DeleteView):
    mixin_text = _('You have not permission to delete task')
    model = models.Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks')


class TaskDetailView(mixins.MyLoginRequired, DetailView):
    model = models.Task
    template_name = 'tasks/task_view.html'
    context_object_name = 'task'


class TaskFilterView(mixins.MyLoginRequired, FilterView):
    filterset_class = filter.TaskFilter
