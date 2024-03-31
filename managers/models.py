from django.db import models
from django.utils import timezone


class Manager(models.Model):
    USER_TYPES = (
        ("recruitment_manager", "Recruitment Manager"),
        ("department_manager", "Department Manager"),
        ("team_lead", "Team Lead"),
    )

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=50)
    user_type = models.CharField(
        max_length=50, choices=USER_TYPES, default="recruitment_manager"
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
