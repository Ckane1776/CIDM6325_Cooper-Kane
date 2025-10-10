from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
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
        self.category = Category.objects.create(name="Test Category")
        self.user = User.objects.create_user(username="testuser", password="password")  # Create a test user
        content_type = ContentType.objects.get_for_model(BlogPost)
        permissions = Permission.objects.filter(content_type=content_type)
        self.user.user_permissions.add(*permissions)  # Assign all BlogPost permissions to the test user
        self.client.login(username="testuser", password="password")  # Log in the test user
        self.blog_post = BlogPost.objects.create(  # Create a blog post for update and delete tests
            title="Test Post",
            content="This is a test post.",
            category=self.category,
            author=self.user,
        )

    def test_blog_post_creation(self):
        response = self.client.post(reverse('blog_create'), {
            'title': 'New Post',
            'content': 'This is a test post.',
            'category': self.category.id,
            'tags': [],  # Optional: Add tags if needed
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        self.assertEqual(BlogPost.objects.count(), 2)  # Ensure the new post is created
        self.assertEqual(BlogPost.objects.last().author, self.user)  # Check if the author is set correctly

    def test_blog_post_update(self):
        response = self.client.post(reverse('blog_edit', args=[self.blog_post.id]), {
            'title': 'Updated Post',
            'content': 'This is an updated test post.',
            'category': self.category.id,
            'tags': [],
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful update
        self.blog_post.refresh_from_db()
        self.assertEqual(self.blog_post.title, 'Updated Post')  # Ensure the title is updated

    def test_blog_post_deletion(self):
        response = self.client.post(reverse('blog_delete', args=[self.blog_post.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect after successful deletion
        self.assertEqual(BlogPost.objects.count(), 0)  # Ensure the post is deleted

    def test_blog_post_form_validation(self):
        response = self.client.post(reverse('blog_create'), {
            'title': '',  # Invalid title (empty)
            'content': 'This is a test post.',
            'category': self.category.id,
            'tags': [],
        })
        self.assertEqual(response.status_code, 200)  # Form should re-render with errors
        self.assertContains(response, 'This field is required.')  # Check for specific error message

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