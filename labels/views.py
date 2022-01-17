from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .models import Label
from django.urls import reverse_lazy
from task_manager import mixins
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class LabelsListView(mixins.MyLoginRequired, ListView):
    model = Label
    template_name = 'labels/labels_list.html'


class LabelCreateView(SuccessMessageMixin, mixins.MyLoginRequired, CreateView):
    model = Label
    template_name = 'labels/label_add.html'
    fields = ['name']
    success_message = _('Label has been successfully created ')
    success_url = reverse_lazy('labels')


class LabelUpdateView(SuccessMessageMixin, mixins.MyLoginRequired, UpdateView):
    model = Label
    template_name = 'labels/label_update.html'
    fields = ['name']
    success_message = _('Label successfully changed')
    success_url = reverse_lazy('labels')


class LabelDeleteView(mixins.OnDeleteMixin, mixins.MyLoginRequired, DeleteView):
    model = Label
    template_name = 'labels/label_delete.html'
    success_url = reverse_lazy('labels')
    text_success = _('Label successfully deleted')
    text_error = _('It is not possible to delete a label because it is in use')
