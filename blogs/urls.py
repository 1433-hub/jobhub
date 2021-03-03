from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employer-profile/', views.employer_profile, name='employer_profile'),
    path('jobseeker-profile/', views.jobseeker_profile, name='jobseeker_profile'),
]