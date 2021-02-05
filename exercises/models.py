from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=32)

class Exercise(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    