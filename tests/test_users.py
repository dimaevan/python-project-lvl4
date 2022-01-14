from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class TestUsers(TestCase):

    def test_edit(self):
        user1 = User.objects.create_user(username='username1', password='password2')
        user2 = User.objects.create_user(username='username2', password='password2')
        self.client.login(username='username1', password='password2')

        response = self.client.get(reverse('update_user', args=[user1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user.html')

        response = self.client.get(reverse('update_user', args=[user2.pk]))
        self.assertEqual(response.status_code, 302)

        response = self.client.post(reverse('update_user', args=[user1.pk]), {
            'username': 'username1', 'first_name': 'User1', 'last_name': ''
        })
        # form = response.context['form']
        # print(form.errors)
        self.assertEqual(response.status_code, 302)
        user1 = User.objects.filter(pk=user1.pk)[0]
        self.assertEqual(user1.first_name, 'User1')
