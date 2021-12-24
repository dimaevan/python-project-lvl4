from django.test import TestCase, LiveServerTestCase
from django.contrib.auth.models import User


class TestViews(LiveServerTestCase):
    def test_login_user(self):
        user = User.objects.create_user(username='dima', password='password')
        data = {'username': user.username, 'password': user.password}
        print(user.is_anonymous)
        self.assertEqual(User.objects.count(), 1)
        response = self.client.post('/login/', data, follow=True)
        print(user.is_authenticated)
        self.assertTemplateUsed(response, 'login.html')
        self.assertRedirects(response, '/login/')

    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertRedirects(response, '/')
