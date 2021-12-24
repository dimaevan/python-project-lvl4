from django.test import TestCase

class TestViews(TestCase):

    def test_login(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'login.html')
        self.assertEqual(response.status_code, 200)

    def test_main(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main_page.html')
        self.assertEqual(response.status_code, 200)

    def test_users(self):
        response = self.client.get('/users/')
        self.assertTemplateUsed(response, 'users.html')
        self.assertEqual(response.status_code, 200)
