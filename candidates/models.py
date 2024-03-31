from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    social_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
