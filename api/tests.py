from django.test import TestCase


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