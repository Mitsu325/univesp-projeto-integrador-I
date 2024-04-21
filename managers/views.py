from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import Manager


def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            manager = Manager.objects.get(email=email)
            if check_password(password, manager.password):
                request.session["manager_id"] = manager.id
                return redirect("management:index")
            else:
                messages.error(request, "E-mail ou senha incorretos.")
        except Manager.DoesNotExist:
            messages.error(request, "E-mail ou senha incorretos.")
    return render(request, "managers/index.html")
