from django.db import models


class Category(models.Model):
    """This class represents category model for a post"""
    name = models.CharField(max_length=30, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
        db_table = 'categories'

    def __str__(self):
        return '{0} - {1} ({2})'.format(self.id, self.name, self.created_at)


class Post(models.Model):
    """This class represents Post model"""
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    category = models.ForeignKey(
        'Category',
        on_delete=models.DO_NOTHING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['created_at']
        db_table = 'posts'

    def __str__(self):
        return '{0} -- ({2}) -- {1}'.format(self.title, self.created_at, self.category.name)
