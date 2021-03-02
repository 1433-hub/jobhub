from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def jobseeker_register(request):
    return render(request, 'accounts/jobseeker_register.html')

def employer_register(request):
    return render(request, 'accounts/employer_register.html')