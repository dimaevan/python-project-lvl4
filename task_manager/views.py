from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
# from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm


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
            return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('main_page')


def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    if request.method == 'POST':
        name = request.POST['username']
        surname = request.POST['surname']
        password = request.POST['password']
        password2 = request.POST['password2']
        nickname = request.POST['nickname']

        if password == password2:
            user = User.objects.create_user(username=nickname, email=None, password=password, first_name=name,
                                            last_name=surname)
            user.save()
        return redirect('main_page')


def delete_user(request):
    return render(request, '')


def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('update_user', user_id=user.pk)
    else:
        form = UserForm(instance=user)

    return render(request, 'user.html', {'form': form})
