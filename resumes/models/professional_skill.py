from django.db import models
from .resume import Resume


class TechnicalSkill(models.Model):
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProfessionalSkill(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="professional_skills"
    )
    technical_skill = models.ForeignKey(TechnicalSkill, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
