from django.shortcuts import render


# TODO: falta implementar a verificação has_resume e imprimir os dados básicos
def index(request):
    has_resume = False
    context = {
        "has_resume": has_resume,
        "menu_items": [
            {"text": "Currículo", "url": "/resumes/"},
            {"text": "Configuração", "url": "/resumes/config"},
        ],
    }
    return render(request, "resumes/index.html", context)


def edit(request):
    has_resume = False
    context = {
        "has_resume": has_resume,
        "menu_items": [
            {"text": "Currículo", "url": "/resumes/"},
            {"text": "Configuração", "url": "/resumes/config"},
        ],
    }
    return render(request, "resumes/edit.html", context)
