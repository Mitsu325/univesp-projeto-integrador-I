from django.urls import path
from . import views

app_name = "management"

urlpatterns = [
    path("", views.index, name="index"),
    path("config", views.config, name="config"),
    path("get_resume", views.get_resume, name="get_resume"),
    path("filter_resumes", views.filter_resumes, name="filter_resumes"),
]
