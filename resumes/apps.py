from django.apps import AppConfig


class ResumesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "resumes"

    def ready(self):
        from .models.resume import Resume
        from .models.area_of_interest import AreaOfInterest
        from .models.gender import Gender
        from .models.address import State, City
        from .models.education_level import EducationLevel
        from .models.education import Education
        from .models.professional_skill import ProfessionalSkill
        from .models.language_skill import LanguageSkill
        from .models.work_experience import WorkExperience
