from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse



class MainView(TemplateView):
    template_name = 'main_page.html'


def users(requests):
    all_users = User.objects.all()
    return render(requests, 'users.html', context={'all_users': all_users})


def login(requests):
    if requests.method == 'GET':
        return render(requests, 'login.html')
    else:
        username = requests.POST['Name']
        return HttpResponse(requests, username)


def logout(requests):
    return render(requests, '')


def registration(requests):
    return render(requests, 'registration.html')


def delete_user(requests):
    return render(requests, '')


def update_user(requests):
    return render(requests, '')
