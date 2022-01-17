from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Status
from .forms import StatusForm
from django.urls import reverse_lazy
from task_manager import mixins
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin


class StatusesListView(mixins.MyLoginRequired, ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'


class StatusCreateView(SuccessMessageMixin, mixins.MyLoginRequired, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/statuses_add.html'
    success_message = _('Status has been successfully created ')
    success_url = reverse_lazy('statuses')


class StatusUpdateView(SuccessMessageMixin, mixins.MyLoginRequired, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/statuses_update.html'
    success_message = _('Status successfully changed')
    success_url = reverse_lazy('statuses')


class StatusDeleteView(mixins.MyLoginRequired, DeleteView):
    model = Status
    template_name = 'statuses/status_delete.html'
    success_url = reverse_lazy('statuses')
    text_success = _('Status successfully deleted')
    text_error = _('It is impossible to delete a status because it is in use ')

    def get_object(self, queryset=None):
        obj = super(StatusDeleteView, self).get_object()
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.count() != 0:
            messages.add_message(self.request, messages.ERROR, self.text_error)
            return redirect('statuses')
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(self.request, messages.INFO, self.text_success)
        return HttpResponseRedirect(success_url)
