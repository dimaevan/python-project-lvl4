from django.test import LiveServerTestCase
from task_manager.models import User


class TestViews(LiveServerTestCase):
    def test_login_user(self):
        self.assertEqual(User.objects.count(), 0)
        user = User.objects.create_user(username='dima', password='password')
        data = {'username': user.username, 'password': user.password}
        self.assertEqual(User.objects.count(), 1)
        response = self.client.post('/login/', data=data, follow=True)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertRedirects(response, '/')
