from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.TextField()
    last_name = models.TextField()
    address_line_one = models.TextField()
    address_line_two = models.TextField()
    city = models.TextField()
    state = models.TextField()
    postal_code = models.IntegerField()
    phone_country_code = models.TextField()
    phone_extension = models.TextField()
    phone_number = models.IntegerField()
    hear_about_us = models.TextField()
    previously_employed_by_company = models.BooleanField()


class Experience(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField()
    company = models.TextField()
    location = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    current_job = models.BooleanField()
    role_description = models.TextField()


class Education(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    university = models.TextField()
    degree = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    major = models.TextField()
    GPA = models.FloatField()
