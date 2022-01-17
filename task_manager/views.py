from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import views as auth_view
from django.utils.translation import gettext as _
from django.contrib.auth import login
from . import forms


class UsersListView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'


class UserSignUpView(SuccessMessageMixin, CreateView):
    form_class = forms.UserSignUpForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')
    success_message = _('User registered successfully')


class UserUpdateView(SuccessMessageMixin, UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/user.html'
    form_class = forms.UserUpdateForm

    success_url = reverse_lazy('users')
    login_url = reverse_lazy('login')
    success_message = _('User successfully changed ')

    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user.username

    def handle_no_permission(self):
        text = _('You have not permission to edit this user.')
        messages.add_message(self.request, messages.WARNING, text)
        return redirect('users')


class UserDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('users')
    login_url = reverse_lazy('login')

    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user.username

    def handle_no_permission(self):
        text = _('You have not permission to edit this user.')
        messages.add_message(self.request, messages.WARNING, text)
        return redirect('users')


class UserLoginView(auth_view.LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        login(self.request, form.get_user())
        text = _('You are login')
        messages.add_message(self.request, messages.SUCCESS, text)
        return redirect('main_page')

    def form_invalid(self, form):
        text = _('Please enter the correct username and password.'
                 ' Both fields may be case sensitive. ')
        messages.add_message(self.request, messages.WARNING, text)
        return redirect('login')


class UserLogout(auth_view.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        text = _('You have successfully logged out.')
        if request.user.is_authenticated:
            messages.info(request, text)
        return super().dispatch(request, *args, **kwargs)
