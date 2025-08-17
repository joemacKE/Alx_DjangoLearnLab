from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post

class AuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertRedirects(response, reverse('profile'))

    def test_logout(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_register(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())


class BlogTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.post = Post.objects.create(title="Django Testing", content="Test content", author=self.user)
        self.post.tags.add("django", "testing")

    def test_post_has_tags(self):
        self.assertIn("django", list(self.post.tags.names()))
    
    def test_search_by_title(self):
        response = self.client.get("/search/?q=Django")
        self.assertContains(response, "Django Testing")

    def test_search_by_tag(self):
        response = self.client.get("/search/?q=django")
        self.assertContains(response, "Django Testing")
