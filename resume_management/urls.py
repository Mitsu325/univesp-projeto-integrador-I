from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("candidates/", include("candidates.urls")),
    path("managers/", include("managers.urls")),
    path("resumes/", include("resumes.urls")),
    path("management/", include("management.urls")),
    path('admin/', admin.site.urls),
]
