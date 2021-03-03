from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def employer_profile(request):
    return render(request, 'users-profile/employer_profile.html')

def jobseeker_profile(request):
    return render(request, 'users-profile/jobseeker_profile.html')