from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from tasks.models import Task


class TestTasks(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

    def test_all_tasks(self):
        Task.objects.create(title='New', author=self.user, text='')
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks_list.html')
        self.assertContains(response, 'New')
        Task.objects.create(title='New1', author=self.user, text='')
        response = self.client.get(reverse('tasks'))
        self.assertContains(response, 'New')
        self.assertContains(response, 'New1')

    def test_add_task(self):
        response = self.client.get(reverse('add_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_add.html')

        response = self.client.post('/tasks/create/', {
            'title': 'MyNewTask',
            'text': 'Just new task',
            'author': self.user.username})
        self.assertContains(response, 'MyNewTask')

    def test_update_task(self):
        new_task = Task.objects.create(title='New', author=self.user, text='')
        self.assertEqual(new_task.pk, 1)

        response = self.client.get(reverse('update_task', args=[new_task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New')
        self.assertTemplateUsed(response, 'tasks/task_update.html')

        response = self.client.post(reverse('update_task', args=[1]),
                                    {'title': 'NewNew', 'text': 'Just new task', 'author': self.user.username}
                                    )
        self.assertEqual(response.status_code, 302)
        task = Task.objects.filter(pk=1)[0]
        self.assertEqual(task.title, 'NewNew')
