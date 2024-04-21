from django.shortcuts import render, redirect


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


def config(request):
    if request.method == "POST":
        if "logout" in request.POST:
            request.session.flush()
            return redirect("candidates:index")
    return render(request, "resumes/config.html")
