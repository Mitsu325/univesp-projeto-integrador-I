from django.db import models
from candidates.models import Candidate
from .area_of_interest import AreaOfInterest
from .gender import Gender
from .address import State, City
from .education_level import EducationLevel


class Resume(models.Model):
    candidate = models.OneToOneField(
        Candidate, on_delete=models.CASCADE, related_name="resume"
    )
    date_of_birth = models.DateField()
    telephone = models.CharField(max_length=15, null=True)
    linkedin = models.CharField(max_length=50, null=True)
    area_of_interest = models.OneToOneField(
        AreaOfInterest, on_delete=models.SET_NULL, null=True
    )
    gender = models.OneToOneField(Gender, on_delete=models.SET_NULL, null=True)
    state = models.OneToOneField(State, on_delete=models.SET_NULL, null=True)
    city = models.OneToOneField(City, on_delete=models.SET_NULL, null=True)
    education_level = models.OneToOneField(
        EducationLevel, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
