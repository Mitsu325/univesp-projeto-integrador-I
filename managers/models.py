from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password


class Manager(models.Model):
    USER_TYPES = (
        ("recruitment_manager", "Recruitment Manager"),
        ("department_manager", "Department Manager"),
        ("team_lead", "Team Lead"),
    )

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    user_type = models.CharField(
        max_length=50, choices=USER_TYPES, default="recruitment_manager"
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
