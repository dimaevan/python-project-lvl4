from django.test import LiveServerTestCase
from django.contrib.auth.models import User


class TestEditUsers(LiveServerTestCase):

    def test_edit(self):
        user1 = User.objects.create_user(username='username1', password='password2')
        user2 = User.objects.create_user(username='username2', password='password2')
        self.client.login(username='username1', password='password2')
        response = self.client.get(f'users//1/update/', {'username': 'Elly'})

