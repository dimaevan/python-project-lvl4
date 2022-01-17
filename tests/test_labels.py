from django.test import TestCase
from django.urls import reverse
from labels.models import Label
from task_manager.models import User


class TestLabels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

    def test_all_labels(self):
        label = Label.objects.create(name='This is Label')
        response = self.client.get(reverse('labels'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/labels_list.html')
        self.assertContains(response, label.name)

    def test_create_label(self):
        response = self.client.get(reverse('create_label'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/label_add.html')

        self.client.post(reverse('create_label'), {'name': 'New label', 'task': ''})
        labels = Label.objects.filter(name='New label')
        self.assertEqual(len(labels), 1)

    def test_update_label(self):
        Label.objects.create(name='Test')
        labels = Label.objects.count()
        self.assertEqual(labels, 1)

        response = self.client.get(reverse('update_label', args=[1, ]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/label_update.html')
        self.assertContains(response, 'Test')

        response = self.client.post(reverse('update_label', args=[1, ]), {'name': 'Update_label'})
        self.assertEqual(response.status_code, 302)

    def test_delete_label(self):
        Label.objects.create(name='Test')
        response = self.client.get(reverse('delete_label', args=[1, ]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/label_delete.html')

        self.client.post(reverse('delete_label', args=[1, ]))
        labels = Label.objects.count()
        self.assertEqual(labels, 0)
