from django.db import models

class Project(models.Model):
    """A model for each project we create"""

    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
