from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from tasks.models import Task
from statuses.models import Status
from labels.models import Label


class TestTasks(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.worker = User.objects.create_user('Dohn', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.status = Status.objects.create(name='New')
        self.label = Label.objects.create(name='New')

    def test_all_tasks(self):
        task1 = Task.objects.create(name='New', author=self.user, description='',
                                    status=self.status, executor=self.worker)
        task1.label.add(self.label)
        task1.save()
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New')
        task2 = Task.objects.create(name='New2', author=self.user, description='',
                                    status=self.status, executor=self.worker)
        task2.label.add(self.label)
        response = self.client.get(reverse('tasks'))
        self.assertContains(response, 'New')
        self.assertContains(response, 'New2')

    def test_add_task(self):
        response = self.client.get(reverse('add_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_add.html')

        response = self.client.post('/tasks/create/', {
            'name': 'MyNewTask',
            'description': 'Just new task',
            'author': self.user.username,
            'worker': self.worker,
            'status': self.status,

        })
        self.assertContains(response, 'MyNewTask')

    def test_update_task(self):
        task1 = Task.objects.create(name='New', author=self.user, description='',
                                    status=self.status, executor=self.worker)
        task1.label.add(self.label)
        task1.save()
        self.assertEqual(task1.pk, 1)

        response = self.client.get(reverse('update_task', args=[task1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New')
        self.assertTemplateUsed(response, 'tasks/task_update.html')
        response = self.client.post(reverse('update_task', args=[1]),
                                    {'name': 'NewNew', 'description': 'Just new task',
                                     'executor': self.worker.id, 'status': self.status.id, }
                                    )
        self.assertEqual(response.status_code, 302)
        task = Task.objects.filter(pk=1)[0]
        self.assertEqual(task.name, 'NewNew')

    def test_delete_task(self):
        task1 = Task.objects.create(name='New', author=self.user, description='',
                                    status=self.status, executor=self.worker)
        task1.label.add(self.label)
        task1.save()
        response = self.client.get(reverse('delete_task', args=[task1.pk]))
        self.assertTemplateUsed(response, 'tasks/task_delete.html')

        response = self.client.post(reverse('delete_task', args=[task1.pk]), )
        self.assertEqual(response.status_code, 302)
        tasks = Task.objects.filter(pk=task1.pk)
        self.assertEqual(len(tasks), 0)

    def test_view_task(self):
        task1 = Task.objects.create(name='New', author=self.user, description='',
                                    status=self.status, executor=self.worker)
        task1.label.add(self.label)
        task1.save()
        response = self.client.get(reverse('view_task', args=[task1.pk]))
        self.assertTemplateUsed(response, 'tasks/task_view.html')
