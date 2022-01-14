from django.test import TestCase
from django.urls import reverse
from statuses.models import Status
from django.contrib.auth.models import User


class TestStatusesViewNoUser(TestCase):
    def test_login_need(self):
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 302)


class TestStatusesView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

    def test_all_statuses(self):
        Status.objects.create(status='New status')
        Status.objects.create(status='New status2')
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses_list.html')
        self.assertContains(response, 'New status')
        self.assertContains(response, 'New status2')
        self.assertNotContains(response, 'Test')

    def test_create_status(self):
        response = self.client.get(reverse('create_status'))
        self.assertTemplateUsed(response, 'statuses/statuses_add.html')
        self.assertEqual(response.status_code, 200)
        self.client.post(reverse('create_status'), {'status': 'new status'})
        query = Status.objects.count()
        self.assertEqual(query, 1)

    def test_edit_status(self):
        status = Status.objects.create(status='Test')
        self.assertEqual(status.pk, 1)
        response = self.client.get(reverse('update_status', args=[status.pk]))
        self.assertTemplateUsed(response, 'statuses/statuses_update.html')

        response = self.client.post(reverse('update_status', args=[status.pk, ]), {'status': 'New test'})
        self.assertEqual(response.status_code, 302)
        status = Status.objects.filter(pk=status.pk)[0]
        self.assertEqual(status.status, 'New test')

    def test_delete_status(self):
        status = Status.objects.create(status='Test')
        response = self.client.get(reverse('delete_status', args=[status.pk]))
        self.assertTemplateUsed(response, 'statuses/status_delete.html')
        response = self.client.post(reverse('delete_status', args=[status.pk]))
        self.assertEqual(response.status_code, 302)
        count = int(Status.objects.count())
        self.assertEqual(count, 0)
