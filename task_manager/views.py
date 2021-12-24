from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user
from .forms import UserForm, RegistrationForm
from django.contrib import messages


class MainView(TemplateView):
    template_name = 'main_page.html'


def users(request):
    all_users = User.objects.all()
    return render(request, 'users.html', context={'all_users': all_users})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            text = 'User don`t found'
            messages.add_message(request, messages.INFO, text)
            return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('main_page')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})


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
            return redirect('update_user', pk=request.user.pk)
    else:
        form = UserForm(instance=this_user)

    return render(request, 'user.html', {'form': form, 'pk': this_user.pk})
