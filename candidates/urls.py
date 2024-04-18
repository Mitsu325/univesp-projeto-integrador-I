from django.urls import path
from .views import HomeCandidates, RegisterCandidates


app_name = 'candidates'

urlpatterns = [
    path('',  HomeCandidates.as_view(), name='homecandidate'),
    path('register/',  RegisterCandidates.as_view(), name='register'),

]
