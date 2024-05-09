from django.shortcuts import render, redirect
from django.db import transaction
from django.http import JsonResponse
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.timesince import timesince
import json
from datetime import datetime
from .models import (
    City,
    Resume,
    Gender,
    State,
    AreaOfInterest,
    WorkExperience,
    JobTitle,
    EducationLevel,
    Education,
    Course,
    ProfessionalSkill,
    LanguageSkill,
)
from candidates.models import Candidate
from .utils import build_edit_context


def index(request):
    candidate_id = request.session.get("candidate_id")
    candidate = Candidate.objects.get(id=candidate_id)

    try:
        resume = Resume.objects.get(candidate=candidate_id)

        date_of_birth = resume.date_of_birth
        today = datetime.now().date()
        age_in_years = (
            today.year
            - date_of_birth.year
            - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        )

        has_resume = True
    except Resume.DoesNotExist:
        resume = Resume()
        has_resume = False
        age_in_years = None

    work_experiences = WorkExperience()
    if has_resume:
        try:
            work_experiences = WorkExperience.objects.filter(resume=resume.id)
        except WorkExperience.DoesNotExist:
            work_experiences = WorkExperience()

    educations = Education()
    if has_resume:
        try:
            educations = Education.objects.filter(resume=resume.id)
        except Education.DoesNotExist:
            educations = Education()

    professional_skills = ProfessionalSkill()
    if has_resume:
        try:
            professional_skills = ProfessionalSkill.objects.filter(resume=resume.id)
        except ProfessionalSkill.DoesNotExist:
            professional_skills = ProfessionalSkill()

    language_skills = LanguageSkill()
    if has_resume:
        try:
            language_skills = LanguageSkill.objects.filter(resume=resume.id)
        except LanguageSkill.DoesNotExist:
            language_skills = LanguageSkill()

    context = {
        "has_resume": has_resume,
        "none_value": "-",
        "menu_items": [
            {"text": "Currículo", "url": "/resumes/"},
            {"text": "Configuração", "url": "/resumes/config"},
        ],
        "candidate": candidate,
        "resume": resume,
        "age_in_years": age_in_years,
        "work_experiences": work_experiences,
        "educations": educations,
        "professional_skills": professional_skills,
        "language_skills": language_skills,
    }
    if "success_message" in request.session:
        success_message = request.session.pop("success_message")
    else:
        success_message = None

    context["success_message"] = success_message

    return render(request, "resumes/index.html", context)


def get_cities(request):
    state_id = request.GET.get("state_id")
    cities = City.objects.filter(state=state_id).values("id", "name")
    return JsonResponse(list(cities), safe=False)


def edit(request):
    if request.method == "POST":
        candidate_id = request.session.get("candidate_id")

        name = request.POST.get("name")
        email = request.POST.get("email")
        social_name = request.POST.get("social_name")

        if not name:
            messages.error(request, "Nome é obrigatório.")
            return redirect("resumes:edit")

        if not email:
            messages.error(request, "E-mail é obrigatório.")
            return redirect("resumes:edit")

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "E-mail inválido.")
            return redirect("resumes:edit")

        if Candidate.objects.exclude(id=candidate_id).filter(email=email).exists():
            messages.error(request, "Este e-mail já está sendo usado.")
            return redirect("resumes:edit")

        candidate = Candidate.objects.get(id=candidate_id)
        candidate.name = name
        candidate.email = email
        candidate.social_name = social_name
        candidate.save()

        telephone = request.POST.get("telephone")
        date_of_birth = request.POST.get("date_of_birth")
        gender_id = request.POST.get("gender")
        gender = Gender.objects.get(id=gender_id)
        linkedin = request.POST.get("linkedin")
        state_id = request.POST.get("state")
        state = State.objects.get(id=state_id)
        city_id = request.POST.get("city")
        city = City.objects.get(id=city_id)
        area_of_interest_id = request.POST.get("area_of_interest")
        area_of_interest = AreaOfInterest.objects.get(id=area_of_interest_id)
        education_level_id = request.POST.get("education_level")
        education_level = EducationLevel.objects.get(id=education_level_id)

        if not date_of_birth:
            messages.error(request, "Data de nascimento é obrigatório.")
            return redirect("resumes:edit")

        if not gender:
            messages.error(request, "Gênero é obrigatório.")
            return redirect("resumes:edit")

        if not state:
            messages.error(request, "Estado é obrigatório.")
            return redirect("resumes:edit")

        if not city:
            messages.error(request, "Cidade é obrigatório.")
            return redirect("resumes:edit")

        if not area_of_interest:
            messages.error(request, "Área de interesse é obrigatório.")
            return redirect("resumes:edit")

        if not education_level:
            messages.error(request, "Grau de escolaridade é obrigatório.")
            return redirect("resumes:edit")

        try:
            resume = Resume.objects.get(candidate=candidate_id)
        except Resume.DoesNotExist:
            resume = Resume(candidate=candidate)

        resume.telephone = telephone
        resume.date_of_birth = date_of_birth
        resume.gender = gender
        resume.linkedin = linkedin
        resume.state = state
        resume.city = city
        resume.area_of_interest = area_of_interest
        resume.education_level = education_level
        resume.save()

        has_work_experience = request.POST.get("has_work_experience")
        valid_work_indexes = json.loads(request.POST.get("valid_work_indexes", "[]"))

        if has_work_experience and not valid_work_indexes:
            messages.error(
                request,
                "Se possui experiência profissional precisa cadastrar pelo menos uma experiência.",
            )
            return redirect("resumes:edit")

        for i in valid_work_indexes:
            work_experience_id = request.POST.get(f"work_experience_id-{i}")
            job_title_id = request.POST.get(f"job_title-{i}")
            job_title = JobTitle.objects.get(id=job_title_id)
            company = request.POST.get(f"company-{i}")
            actual_job = request.POST.get(f"actual_job-{i}")
            work_start_date = request.POST.get(f"work_start_date-{i}")
            work_end_date = request.POST.get(f"work_end_date-{i}")
            description = request.POST.get(f"description-{i}")

            if actual_job:
                work_end_date = None
            else:
                work_end_date = request.POST.get(f"work_end_date-{i}")

            if work_experience_id:
                work_experience = WorkExperience.objects.get(id=work_experience_id)
                work_experience.job_title = job_title
                work_experience.company = company
                work_experience.start_date = work_start_date
                work_experience.end_date = work_end_date
                work_experience.description = description
                work_experience.save()
            else:
                work_experience = WorkExperience(
                    resume=resume,
                    job_title=job_title,
                    company=company,
                    start_date=work_start_date,
                    end_date=work_end_date,
                    description=description,
                )
                work_experience.save()

        valid_education_indexes = json.loads(
            request.POST.get("valid_education_indexes", "[]")
        )

        print("valid_education_indexes", valid_education_indexes)

        if not valid_education_indexes:
            messages.error(
                request,
                "É obrigatório o preenchimento de pelo menos uma formação acadêmica.",
            )
            return redirect("resumes:edit")

        for i in valid_education_indexes:
            education_id = request.POST.get(f"education_id-{i}")
            degree = request.POST.get(f"degree-{i}")
            course_id = request.POST.get(f"course-{i}")
            institution = request.POST.get(f"institution-{i}")
            actual_course = request.POST.get(f"actual_course-{i}")
            course_start_date = request.POST.get(f"course_start_date-{i}")
            course_end_date = request.POST.get(f"course_end_date-{i}")

            course = None
            if course_id:
                course = Course.objects.get(id=course_id)

            if actual_course:
                course_end_date = None
            else:
                course_end_date = request.POST.get(f"course_end_date-{i}")

            if education_id:
                work_experience = Education.objects.get(id=education_id)
                work_experience.degree = degree
                work_experience.course = course
                work_experience.institution = institution
                work_experience.start_date = course_start_date
                work_experience.end_date = course_end_date
                work_experience.save()
            else:
                work_experience = Education(
                    resume=resume,
                    degree=degree,
                    course=course,
                    institution=institution,
                    start_date=course_start_date,
                    end_date=course_end_date,
                )
                work_experience.save()

        request.session["success_message"] = "Informações atualizadas com sucesso."
        return redirect("resumes:index")

    context = build_edit_context(request)
    return render(request, "resumes/edit.html", context)


def config(request):
    context = {
        "menu_items": [
            {"text": "Currículo", "url": "/resumes/"},
            {"text": "Configuração", "url": "/resumes/config"},
        ],
    }
    if request.method == "POST":
        if "logout" in request.POST:
            request.session.flush()
            return redirect("candidates:index")
    return render(request, "resumes/config.html", context)
