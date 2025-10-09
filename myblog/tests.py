from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from django.utils.timezone import now
from .models import BlogPost, Category

class BlogViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='testpassword')

        self.category = Category.objects.create(name="Test Category")
        self.blog_post = BlogPost.objects.create(
            title="Test Post",
            content="Test content",
            published_date=now(),
            author=self.user,
            category=self.category
        )

    def test_blog_list_displays_posts(self):
        self.client.login(username='tester', password='testpassword')
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

class BlogPostCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='testpassword')
        self.category = Category.objects.create(name="Test Category")
        self.blog_post = BlogPost.objects.create(
            title="Test Post",
            content="Test content",
            published_date=now(),
            author=self.user,
            category=self.category
        )
        permissions = Permission.objects.filter(content_type__app_label='myblog', codename__in=[
            'add_blogpost', 'change_blogpost', 'delete_blogpost'
        ])
        self.user.user_permissions.add(*permissions)

    def test_blog_post_creation(self):
        self.client.login(username='tester', password='testpassword')
        response = self.client.post(reverse('blog_create'), {
            'title': 'New Post',
            'content': 'New Content',
            'published_date': now(),  # Added published_date field
            'author': self.user.id,
            'category': self.category.id
        })
        if response.status_code == 200 and response.context:
            print(response.context['form'].errors)  # Debugging: Print form errors
        self.assertEqual(response.status_code, 302)
        self.assertTrue(BlogPost.objects.filter(title='New Post').exists())

    def test_blog_post_update(self):
        self.client.login(username='tester', password='testpassword')
        response = self.client.post(reverse('blog_edit', args=[self.blog_post.id]), {
            'title': 'Updated Post',
            'content': 'Updated Content',
            'published_date': now(),  # Added published_date field
            'author': self.user.id,
            'category': self.category.id
        })
        if response.status_code == 200 and response.context:
            print(response.context['form'].errors)  # Debugging: Print form errors
        self.assertEqual(response.status_code, 302)
        self.blog_post.refresh_from_db()
        self.assertEqual(self.blog_post.title, 'Updated Post')

    def test_blog_post_deletion(self):
        self.client.login(username='tester', password='testpassword')
        response = self.client.post(reverse('blog_delete', args=[self.blog_post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(BlogPost.objects.filter(id=self.blog_post.id).exists())

class BlogPostPermissionTests(TestCase):
    def setUp(self):
        self.user_with_permission = User.objects.create_user(username='admin', password='adminpassword')

        self.user_without_permission = User.objects.create_user(username='tester', password='testpassword')

        self.category = Category.objects.create(name="Test Category")
        self.blog_post = BlogPost.objects.create(
            title="Test Post",
            content="Test content",
            published_date=now(),
            author=self.user_with_permission,
            category=self.category
        )

        # Assign permissions to the admin user
        permissions = Permission.objects.filter(codename__in=['delete_blogpost'])
        self.user_with_permission.user_permissions.add(*permissions)

    def test_user_with_permission_can_delete(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(reverse('blog_delete', args=[self.blog_post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(BlogPost.objects.filter(id=self.blog_post.id).exists())

    def test_user_without_permission_cannot_delete(self):
        self.client.login(username='tester', password='testpassword')
        response = self.client.post(reverse('blog_delete', args=[self.blog_post.id]))
        self.assertEqual(response.status_code, 403)
        self.assertTrue(BlogPost.objects.filter(id=self.blog_post.id).exists())