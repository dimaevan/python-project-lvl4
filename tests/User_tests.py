import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('John', email=None, password='Password')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_login(client, django_user_model):
    user = User.objects.create_user(
        username='someone', password='password'
    )
    assert user.pk == 1
    client.login(user)
