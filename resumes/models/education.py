from django.db import models
from .resume import Resume


class Course(models.Model):
    COURSE_TYPES = (
        ("technical", "Technical"),
        ("higher_education", "Higher Education"),
    )
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=2)
    course_type = models.CharField(max_length=50, choices=COURSE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Education(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="educations"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    institution = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
