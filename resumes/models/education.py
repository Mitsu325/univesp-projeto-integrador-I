from django.db import models
from .resume import Resume


class Course(models.Model):
    COURSE_TYPES = (
        ("technical", "Técnico"),
        ("higher_education", "Ensino Superior"),
    )
    name = models.CharField(max_length=200)
    course_type = models.CharField(max_length=50, choices=COURSE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Education(models.Model):
    DEGREE_TYPES = (
        ("elementary", "Fundamental"),
        ("high_school", "Ensino Médio"),
        ("technical", "Técnico"),
        ("bachelor", "Bacharelado"),
        ("teaching", "Licenciatura"),
        ("technologist", "Tecnólogo"),
        ("master", "Mestrado"),
        ("doctorate", "Doutorado"),
        ("post_doctorate", "Pós-Doutorado"),
        ("other", "Outros"),
    )
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="educations"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    institution = models.CharField(max_length=50)
    degree = models.CharField(max_length=50, choices=DEGREE_TYPES, default="other")
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
