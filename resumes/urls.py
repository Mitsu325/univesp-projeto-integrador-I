from django.urls import path

from . import views

app_name = "resumes"

urlpatterns = [
    path("", views.index, name="index"),
    path("edit", views.edit, name="edit"),
    path("config", views.config, name="config"),
    path("get_cities", views.get_cities, name="get_cities"),
]
