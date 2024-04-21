from django.urls import path
from . import views

app_name = "management"

urlpatterns = [
    path("", views.index, name="index"),
]

urlpatterns = [
    path("config", views.config, name="config"),
]
