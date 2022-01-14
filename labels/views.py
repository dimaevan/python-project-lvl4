from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .models import Label
from django.urls import reverse_lazy


class LabelsListView(ListView):
    model = Label
    template_name = 'labels/labels_list.html'


class LabelCreateView(CreateView):
    model = Label
    template_name = 'labels/label_add.html'
    fields = ['name']
    success_url = reverse_lazy('labels')


class LabelUpdateView(UpdateView):
    model = Label
    template_name = 'labels/label_update.html'
    fields = ['name']
    success_url = reverse_lazy('labels')


class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'labels/label_delete.html'
    success_url = reverse_lazy('labels')
