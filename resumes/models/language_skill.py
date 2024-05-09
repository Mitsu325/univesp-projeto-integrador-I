from django.db import models
from .resume import Resume


class Language(models.Model):
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LanguageSkill(models.Model):
    LEVEL_TYPES = (
        ("basic", "Básico"),
        ("intermediate", "Intermediário"),
        ("advanced", "Avançado"),
    )
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, related_name="language_skills"
    )
    level = models.CharField(max_length=50, choices=LEVEL_TYPES)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
