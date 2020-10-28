from django.db import models
from django.conf import settings


class Job(models.Model):
    url = models.URLField()
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    # Need to add location information to this model
