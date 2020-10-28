from django.db import models
from jobs.models import Job
from django.contrib.auth import get_user_model


class Application(models.Model):
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    status = models.TextField()
    description = models.TextField(blank=True)
