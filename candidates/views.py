from django.shortcuts import render


def index(request):
    return render(request, "candidates/index.html")


def register(request):
    return render(request, "candidates/register.html")
