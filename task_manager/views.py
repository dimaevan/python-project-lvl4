from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User


class MainView(TemplateView):
    template_name = 'main_page.html'


def users(requests):
    all_users = User.objects.all()
    return render(requests, 'users.html', context={'all_users': all_users})


def login(requests):
    return render(requests, 'login.html')


def logout(requests):
    pass


def registration(requests):
    pass


def delete_user(requests):
    pass


def update_user(requests):
    pass
