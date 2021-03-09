from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('employer-profile/', views.employer_profile, name='employer_profile'),
    path('jobseeker-profile/', views.jobseeker_profile, name='jobseeker_profile'),
    path('jobseeker-profile-update/', views.jobseeker_profile_update, name='jobseeker_profile_update'),
    path('jobseeker-skill-update/', views.jobseeker_skill_update, name='jobseeker_skill_update'),
    path('jobseeker-language-update/', views.jobseeker_language_update, name='jobseeker_language_update'),
    path('jobseeker-education-update/', views.jobseeker_education_update, name='jobseeker_education_update'),
    path('jobseeker-employment-update/', views.jobseeker_employment_update, name='jobseeker_employment_update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)