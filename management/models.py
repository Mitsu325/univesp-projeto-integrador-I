from django.db import models
from managers.models import Manager
from candidates.models import Candidate


class Interview(models.Model):
    STATUS_TYPES = (
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("pending", "Pending"),
    )
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    interview_date = models.DateTimeField()
    duration_minutes = models.DurationField()
    approval_status = models.CharField(
        max_length=25, choices=STATUS_TYPES, default="pending"
    )
    reason = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
