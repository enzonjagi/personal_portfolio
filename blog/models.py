from django.db import models

class Category(models.Model):
    """A model dedicated to categorizing Blog Posts"""

    name = models.CharField(max_length=20)


class Post(models.Model):
    """A model for individual Blog Posts"""

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        'Category',
        related_name='posts',
    )

class Comment(models.Model):
    """Allows users to add comments below posts"""

    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)