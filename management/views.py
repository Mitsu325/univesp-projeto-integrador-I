from django.shortcuts import render, redirect


def index(request):
    context = {
        "menu_items": [
            {"text": "Candidatos", "url": "/management/"},
            {"text": "Configuração", "url": "/management/config"},
        ],
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
