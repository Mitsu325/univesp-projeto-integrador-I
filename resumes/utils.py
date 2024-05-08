from .models import (
    Resume,
    Gender,
    AreaOfInterest,
    State,
    JobTitle,
    WorkExperience,
    EducationLevel,
    Course,
    Education,
    TechnicalSkill,
    ProfessionalSkill,
    Language,
    LanguageSkill,
)
from candidates.models import Candidate


def get_resume_context(candidate_id):
    try:
        candidate = Candidate.objects.get(id=candidate_id)
        resume = Resume.objects.get(candidate=candidate_id)
    except Resume.DoesNotExist:
        resume = Resume()

    return resume, candidate


def get_work_experiences(resume):
    if resume:
        work_experiences = WorkExperience.objects.filter(resume=resume.id)
        if work_experiences:
            return work_experiences, True
    return WorkExperience.objects.none(), False


def get_educations(resume):
    if resume:
        return Education.objects.filter(resume=resume.id)
    return Education.objects.none()


def get_professional_skills(resume):
    if resume:
        return ProfessionalSkill.objects.filter(resume=resume.id)
    return ProfessionalSkill.objects.none()


def get_language_skills(resume):
    if resume:
        return LanguageSkill.objects.filter(resume=resume.id)
    return LanguageSkill.objects.none()


def get_courses_by_type(course_type):
    return Course.objects.filter(course_type=course_type).values("id", "name")


def build_edit_context(request):
    candidate_id = request.session.get("candidate_id")
    genders = Gender.objects.all()
    area_of_interests = AreaOfInterest.objects.all()
    states = State.objects.all()
    job_titles = JobTitle.objects.all()
    education_levels = EducationLevel.objects.all()
    technical_skills = TechnicalSkill.objects.all()
    languages = Language.objects.all()
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

    resume, candidate = get_resume_context(candidate_id)
    work_experiences, has_work_experience = get_work_experiences(resume)
    educations = get_educations(resume)
    professional_skills = get_professional_skills(resume)
    language_skills = get_language_skills(resume)

    context = {
        "menu_items": [
            {"text": "Currículo", "url": "/resumes/"},
            {"text": "Configuração", "url": "/resumes/config"},
        ],
        "resume": resume,
        "candidate": candidate,
        "work_experiences": work_experiences,
        "educations": educations,
        "professional_skills": professional_skills,
        "language_skills": language_skills,
        "has_work_experience": has_work_experience,
        "genders": genders,
        "area_of_interests": area_of_interests,
        "states": states,
        "job_titles": job_titles,
        "education_levels": education_levels,
        "technical_skills": technical_skills,
        "languages": languages,
        "technical_courses": get_courses_by_type("technical"),
        "higher_education_courses": get_courses_by_type("higher_education"),
        "DEGREE_TYPES": DEGREE_TYPES,
    }

    return context
