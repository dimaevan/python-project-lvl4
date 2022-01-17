from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


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
