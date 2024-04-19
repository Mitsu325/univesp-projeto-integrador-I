from django.shortcuts import render


def index(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")
