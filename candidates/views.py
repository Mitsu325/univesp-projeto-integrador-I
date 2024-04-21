import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import Candidate


def validate_password(password):
    if not re.match(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
        password,
    ):
        return False
    return True


def index(request):
    return render(request, "candidates/index.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        print(password)
        print(confirm_password)

        if not name:
            messages.error(request, "Nome é obrigatório.")
            return redirect("candidates:register")

        if not email:
            messages.error(request, "E-mail é obrigatório.")
            return redirect("candidates:register")

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "E-mail inválido.")
            return redirect("candidates:register")

        if not password:
            messages.error(request, "Senha é obrigatória.")
            return redirect("candidates:register")

        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect("candidates:register")

        if not validate_password(password):
            messages.error(
                request,
                "A senha deve conter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.",
            )
            return redirect("candidates:register")

        if Candidate.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está sendo usado.")
            return redirect("candidates:register")

        candidate = Candidate(name=name, email=email, password=make_password(password))
        print(candidate)
        candidate.save()

        messages.success(
            request, "Cadastro realizado com sucesso. Faça login para continuar."
        )
        return redirect("candidates:index")
    return render(request, "candidates/register.html")
