from django.shortcuts import render, redirect
from .forms import UserSignUpForm, EmployerSignUpForm
from .models import Employer
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
import uuid
from django.conf import settings
from django.contrib.auth.models import User



# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

    

def jobseeker_register(request):
    return render(request, 'accounts/jobseeker_register.html')

#employer registration
# create object of user and employer
#  
def employer_register(request):
    user_form = UserSignUpForm()
    employer_form = EmployerSignUpForm()
    context = {
        'user_form': user_form,
        'employer_form': employer_form
    }
    try:
        if request.method == 'POST':
            user_form = UserSignUpForm(request.POST)
            employer_form = EmployerSignUpForm(request.POST)

            if user_form.is_valid() and employer_form.is_valid():
                user_form.is_employer = True
                user_form.is_active = False
                email = request.POST.get('email')
                # print(email)
                user_form.save()

                industry_type = request.POST.get('industry_type')
                # print(industry_type)
                
                token = str(uuid.uuid4())


                # print(token)
                employer_profile = Employer.objects.create(user=user_form.instance, token = token)
                employer_profile.save()


                activate(email, token)

    except Exception as e:
        print(e)

    
    return render(request, 'accounts/employer_register.html', context)
    
#send an activation email
def activate(email, token):
    mail_subject = 'Activate your account.'
    message = f'Please click on the link to confirm your registration, http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    list = [email]
    send_mail(mail_subject, message, email_from, list)

#to verify email account 
def verify(request, token):
    try:
        employer_object = Employer.objects.filter(token=token).first()
        if employer_object:
            employer_object.is_employer = True
            employer_object.save()
            print('Your account is verified')
            return redirect('home')
        else:
            return redirect('/')

    except Exception as e:
        print(e)


def employer_login(request):
    return render(request, 'accounts/employer_login.html')

    # if request.method == 'POST':
    #     email = request.POST.get['email']
    #     password = request.POST.get['password']
    #     print(email, password)
    #     user = authenticate(request, email=email, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         return render(request, 'accounts/login.html')
    