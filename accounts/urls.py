from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('employer-registration/', views.employer_register, name='employer_register'),
    path('login/employer/', views.employer_login, name='employer_login'),

    path('jobseeker-registration/', views.jobseeker_register, name='jobseeker_register'),
    path('login/jobseeker/', views.jobseeker_login, name='jobseeker_login'),
    
    path('change-password/', views.change_password, name='change_password'),

]