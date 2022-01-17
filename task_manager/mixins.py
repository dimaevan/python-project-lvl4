from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect


class MyLoginRequired(LoginRequiredMixin):
    login_url = reverse_lazy('login')


class StatusesLoginRequired(LoginRequiredMixin):
    login_url = reverse_lazy('login')


class MyTaskMixin(UserPassesTestMixin, MyLoginRequired):
    mixin_text = _('You have not permission to do this')

    def test_func(self):
        obj = self.get_object()
        return obj.author.id == self.request.user.id

    def handle_no_permission(self):
        messages.add_message(self.request, messages.ERROR, self.mixin_text)
        return redirect('tasks')


class OnDeleteMixin(DeleteView):
    text_success = ''
    text_error = ''

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.count() != 0:
            messages.add_message(self.request, messages.ERROR, self.text_error)
            return redirect('labels')
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(self.request, messages.INFO, self.text_success)
        return HttpResponseRedirect(success_url)
