from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Status
from .forms import StatusForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class StatusesListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Status
    template_name = 'statuses/statuses_list.html'


class StatusCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Status
    form_class = StatusForm
    template_name = 'statuses/statuses_add.html'
    success_url = reverse_lazy('statuses')


class StatusDetailView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Status
    form_class = StatusForm
    template_name = 'statuses/statuses_update.html'
    success_url = reverse_lazy('statuses')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Status
    template_name = 'statuses/status_delete.html'
    success_url = reverse_lazy('statuses')




