from django.db import models


class EducationLevel(models.Model):
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
