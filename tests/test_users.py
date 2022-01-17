from django.test import TestCase
from task_manager.models import User
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
            'username': 'username1', 'first_name': 'User1', 'last_name': 'Last',
            'password1': user1.password, 'password2': user1.password
        })
        # form = response.context['form']
        # print(form.errors)
        self.assertEqual(response.status_code, 302)
        user1 = User.objects.filter(pk=user1.pk)[0]
        self.assertEqual(user1.first_name, 'User1')

    def test_register_user(self):
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registration.html')

        response = self.client.post(reverse('registration'), {'username': 'username1',
                                                              'first_name': 'User',
                                                              'last_name': 'Last',
                                                              'password1': '12341234',
                                                              'password2': '12341234'})
        my_user = User.objects.filter(username='username1')[0]
        self.assertEqual(my_user.username, 'username1')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
