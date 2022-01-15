from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .models import Label
from django.urls import reverse_lazy
from task_manager import mixins


class LabelsListView(mixins.MyLoginRequired, ListView):
    model = Label
    template_name = 'labels/labels_list.html'


class LabelCreateView(mixins.MyLoginRequired, CreateView):
    model = Label
    template_name = 'labels/label_add.html'
    fields = ['name']
    success_url = reverse_lazy('labels')


class LabelUpdateView(mixins.MyLoginRequired, UpdateView):
    model = Label
    template_name = 'labels/label_update.html'
    fields = ['name']
    success_url = reverse_lazy('labels')


class LabelDeleteView(mixins.MyLoginRequired, DeleteView):
    model = Label
    template_name = 'labels/label_delete.html'
    success_url = reverse_lazy('labels')
