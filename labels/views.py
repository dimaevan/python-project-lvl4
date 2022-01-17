from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .models import Label
from django.urls import reverse_lazy
from task_manager import mixins
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect


class LabelsListView(mixins.MyLoginRequired, ListView):
    model = Label
    template_name = 'labels/labels_list.html'


class LabelCreateView(mixins.MyLoginRequired, CreateView):
    model = Label
    template_name = 'labels/label_add.html'
    fields = ['name']
    success_url = reverse_lazy('labels')

    def form_valid(self, form):
        text = _('The label has been successfully created ')
        messages.add_message(self.request, messages.SUCCESS, text)
        form.save()
        return redirect('statuses')


class LabelUpdateView(mixins.MyLoginRequired, UpdateView):
    model = Label
    template_name = 'labels/label_update.html'
    fields = ['name']
    success_url = reverse_lazy('labels')


class LabelDeleteView(mixins.MyLoginRequired, DeleteView):
    model = Label
    template_name = 'labels/label_delete.html'
    success_url = reverse_lazy('labels')
    text_success = _('Label successfully deleted')
    text_error = _('It is not possible to delete a label because it is in use')

    def get_object(self, queryset=None):
        obj = super(LabelDeleteView, self).get_object()
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.count() != 0:
            messages.add_message(self.request, messages.ERROR, self.text_error)
            return redirect('labels')
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(self.request, messages.INFO, self.text_success)
        return HttpResponseRedirect(success_url)
