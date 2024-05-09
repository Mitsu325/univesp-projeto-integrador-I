from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from resumes.models import (
    Resume,
    AreaOfInterest,
    State,
    JobTitle,
    EducationLevel,
    TechnicalSkill,
    WorkExperience,
)
from django.db.models import Min, OuterRef, Subquery
from datetime import datetime


def filter_resumes(request):
    area_of_interest_id = request.GET.get("area_of_interest_id")
    latest_start_date = (
        WorkExperience.objects.filter(
            resume_id=OuterRef("id"), resume__area_of_interest_id=area_of_interest_id
        )
        .order_by("-start_date")
        .values("start_date")[:1]
    )

    resumes = (
        Resume.objects.annotate(
            latest_experience_start_date=Subquery(latest_start_date)
        )
        .filter(area_of_interest_id=area_of_interest_id)
        .order_by("id")
    )

    resume_data = {"data": []}
    for resume in resumes.all():
        candidate_name = (
            resume.candidate.social_name
            if resume.candidate.social_name
            else resume.candidate.name
        )
        job_title = (
            resume.work_experiences.first().job_title.title
            if resume.work_experiences.exists()
            else ""
        )
        data = {
            "id": resume.id,
            "candidate_name": candidate_name,
            "area_of_interest": resume.area_of_interest.name,
            "job_title": job_title,
        }
        resume_data["data"].append(data)

    return JsonResponse(resume_data, safe=False)


def get_resume(request):
    resume_id = request.GET.get("resume_id")
    resume = Resume.objects.get(id=resume_id)
    date_of_birth = resume.date_of_birth
    today = datetime.now().date()
    age_in_years = (
        today.year
        - date_of_birth.year
        - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    )

    resume_data = {
        "id": resume.id,
        "candidate": {
            "name": resume.candidate.name,
            "social_name": resume.candidate.social_name,
            "email": resume.candidate.email,
        },
        "age_in_years": age_in_years,
        "telephone": resume.telephone,
        "linkedin": resume.linkedin,
        "area_of_interest": resume.area_of_interest.name,
        "gender": resume.gender.name,
        "state": resume.state.abbreviation,
        "city": resume.city.name,
        "education_level": resume.education_level.name,
        "work_experiences": [],
        "educations": [],
        "professional_skills": [],
        "language_skills": [],
    }

    for work_experience in resume.work_experiences.all():
        experience_data = {
            "job_title": work_experience.job_title.title,
            "company": work_experience.company,
            "start_date": work_experience.start_date,
            "end_date": work_experience.end_date,
            "description": work_experience.description,
        }
        resume_data["work_experiences"].append(experience_data)

    for education in resume.educations.all():
        course_name = education.course.name if education.course else ""
        education_data = {
            "degree": education.get_degree_display(),
            "course": course_name,
            "institution": education.institution,
            "start_date": education.start_date,
            "end_date": education.end_date,
        }
        resume_data["educations"].append(education_data)

    for professional_skill in resume.professional_skills.all():
        professional_skill_data = {
            "technical_skill": professional_skill.technical_skill.name,
        }
        resume_data["professional_skills"].append(professional_skill_data)

    for language_skill in resume.language_skills.all():
        language_skill_data = {
            "language": language_skill.language.name,
            "level": language_skill.get_level_display(),
        }
        resume_data["language_skills"].append(language_skill_data)

    return JsonResponse(resume_data, safe=False)


def index(request):
    try:
        resumes = Resume.objects.annotate(
            earliest_work_experience=Min("work_experiences__start_date")
        ).order_by("earliest_work_experience")
    except Resume.DoesNotExist:
        resumes = Resume()

    area_of_interests = AreaOfInterest.objects.all()
    states = State.objects.all()
    job_titles = JobTitle.objects.all()
    education_levels = EducationLevel.objects.all()
    technical_skills = TechnicalSkill.objects.all()

    context = {
        "menu_items": [
            {"text": "Candidatos", "url": "/management/"},
            {"text": "Configuração", "url": "/management/config"},
        ],
        "resumes": resumes,
        "area_of_interests": area_of_interests,
        "states": states,
        "job_titles": job_titles,
        "education_levels": education_levels,
        "technical_skills": technical_skills,
    }
    return render(request, "management/index.html", context)


def config(request):
    context = {
        "menu_items": [
            {"text": "Candidatos", "url": "/resumes/"},
            {"text": "Configuração", "url": "/resumes/config"},
        ],
    }
    if request.method == "POST":
        if "logout" in request.POST:
            request.session.flush()
            return redirect("managers:index")
    return render(request, "management/config.html", context)
