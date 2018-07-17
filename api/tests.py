from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


from .models import Category, Post


class CategoryTestCase(TestCase):
    """This class defines the test suit for Category model"""

    def setUp(self):
        """Set up new category for further usage in test methods"""
        self.category_name = 'Some category'
        self.category = Category(name=self.category_name)

    def test_model_can_create_a_category(self):
        """Tests if a category can be created"""
        old_count = Category.objects.count()
        self.category.save()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)


class PostTestCase(TestCase):
    """This class represents the test suit for Post model"""

    def setUp(self):
        """Set up new post for further usage in test methods"""
        category_name = 'Some category'
        self.category = Category(name=category_name)
        self.category.save()

        post_title = 'Some title'
        post_content = 'Some content'
        self.post = Post.objects.create(
            title=post_title,
            content=post_content,
            category=self.category,
        )

    def test_post_creation(self):
        """Tests if the a post can be created"""
        self.assertEqual(self.post.title, 'Some title')
        self.assertEqual(self.post.category, self.category)


class CategoryViewTestCase(TestCase):
    """Test suit for Category api view"""

    def setUp(self):
        """Set up client, category and try to create via post request"""
        self.client = APIClient()
        category_name = 'Some category'
        self.category_data = {
            'name': category_name,
        }
        self.response = self.client.post(
            reverse('create-category'),
            self.category_data,
            format='json',
        )

    def test_api_can_create_category(self):
        """Test api can create category"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class PostViewTestCase(TestCase):
    """Test suit for Post api view"""

    def setUp(self):
        """Set up client, post and try to create via post request"""
        self.client = APIClient()
        self.post_data = {
            'id': 2,
            'title': 'Test post title',
            'content': 'Some content for a post',
            'category': {
                'id': 3,
                'name': 'Test category name',
            }
        }
        self.response = self.client.post(
            reverse('create-post'),
            self.post_data,
            format='json',
        )

    def test_api_can_create_post(self):
        """Test api can create post"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)