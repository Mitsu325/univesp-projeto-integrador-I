from django.shortcuts import render


def index(request):
    has_resume = False
    context = {
        "has_resume": has_resume,
        "menu_items": [
            {"text": "Currículo", "url": "/resumes/"},
            {"text": "Configuração", "url": "/resumes/config"},
        ],
    }
    return render(request, "index.html", context)
