from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    social_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
