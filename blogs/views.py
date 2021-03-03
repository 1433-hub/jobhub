from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def employer_profile(request):
    return render(request, 'users-profile/employer_profile.html')

    
@login_required
def jobseeker_profile(request):
    return render(request, 'users-profile/jobseeker_profile.html')