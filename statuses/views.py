from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Status
from .forms import StatusForm
from django.urls import reverse_lazy
from task_manager import mixins


class StatusesListView(mixins.MyLoginRequired, ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'


class StatusCreateView(mixins.MyLoginRequired, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/statuses_add.html'
    success_url = reverse_lazy('statuses')


class StatusDetailView(mixins.MyLoginRequired, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/statuses_update.html'
    success_url = reverse_lazy('statuses')


class StatusDeleteView(mixins.MyLoginRequired, DeleteView):
    model = Status
    template_name = 'statuses/status_delete.html'
    success_url = reverse_lazy('statuses')
