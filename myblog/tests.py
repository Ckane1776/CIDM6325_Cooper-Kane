from django.test import TestCase
from django.urls import reverse
from .models import BlogPost

class BlogViewTests(TestCase):
    def setUp(self):
        BlogPost.objects.create(title="Test Post", content="Test content")

    def test_blog_view_displays_posts(self):
        response = self.client.get(reverse('blog_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")