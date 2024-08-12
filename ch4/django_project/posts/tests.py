from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text=f'This is a test...')

    def test_model_content(self):
        self.assertEqual(self.post.text, 'This is a test...')

    def test_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # New method
    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'This is a test...')
