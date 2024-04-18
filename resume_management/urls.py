from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('candidates.urls',)),
    path("managers/", include("managers.urls")),
    path("resumes/", include("resumes.urls")),
    path("management/", include("management.urls")),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
