from django.db import models
from .resume import Resume


class JobTitle(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WorkExperience(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="work_experiences"
    )
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
