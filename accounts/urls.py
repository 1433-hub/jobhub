from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('employer-registration/', views.employer_register, name='employer_register'),
    path('jobseeker-registration/', views.jobseeker_register, name='jobseeker_register'),
    path('login/', views.login, name='login'),
    
]