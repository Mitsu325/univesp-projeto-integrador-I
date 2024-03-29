from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("candidates/", include("candidates.urls")),
    path('admin/', admin.site.urls),
]
