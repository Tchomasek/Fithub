from django.db import models

class Exercise(models.Model):
    content = models.TextField(blank=True, null=True)
    