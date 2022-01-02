from django.views.generic import TemplateView, UpdateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.views.generic.list import ListView
from django.contrib.auth import get_user
from .forms import UserForm
from django.views import View


class MainView(TemplateView):
    template_name = 'main_page.html'


class UsersDetailView(ListView):
    model = User
    template_name = 'users.html'


class RegisterView(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))

    def get(self, request):
        return render(request, 'registration.html', {'form': UserCreationForm})


def delete_user(request, pk):
    if request.method == 'POST':
        u = User.objects.get(id=pk)
        u.delete()
        return redirect('main_page')

    return render(request, 'delete_user.html')


def update_user(request, pk):
    this_user = get_object_or_404(User, pk=pk)
    login_user = get_user(request).pk
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid() and this_user.pk == login_user:
            user = form.save()
            user.save()
            return redirect('users')
    else:
        form = UserForm(instance=this_user)

    return render(request, 'user.html', {'form': form, 'pk': this_user.pk})
