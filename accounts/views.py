from django.shortcuts import render, redirect
from .forms import UserSignUpForm, EmployerSignUpForm, JobseekerSignUpForm
from .models import Employer, Jobseeker
from django.contrib.auth import authenticate, login as loggedin, logout
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
import uuid
from django.conf import settings
from django.contrib.auth.models import User


from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



# sign up 
def signup(request):
    return render(request, 'accounts/signup.html')

#login
def login(request):
    return render(request, 'accounts/login.html')

    
#jobseeker sign
# create an object of jobseeker and User
# send email to user
def jobseeker_register(request):
    user_form = UserSignUpForm()
    jobseeker_form = JobseekerSignUpForm()
    context = {
        'user_form': user_form,
        'jobseeker_form': jobseeker_form
    }
    try:
        if request.method == 'POST':
            user_form = UserSignUpForm(request.POST)
            jobseeker_form = JobseekerSignUpForm(request.POST)
            if user_form.is_valid() and jobseeker_form.is_valid():
                user_form.is_active = False
                email = request.POST.get('email')
                # print(email)

                gender = request.POST.get('gender')
                # print(gender)

                job_category = request.POST.get('job_category')
                # print(job_category)
                user_form.save()
                token = str(uuid.uuid4())

                jobseeker_profile = Jobseeker.objects.create(user=user_form.instance, token = token, gender=gender, job_category=job_category)
                jobseeker_profile.save()
                jobseeker_activate(email, token)
                messages.add_message(request, messages.INFO, 'Please check your email to verify your Account!')
                return redirect('jobseeker_register')

            else:
                messages.add_message(request, messages.ERROR, 'This username is already taken!')
    except Exception as e:
        print(e)

    return render(request, 'accounts/jobseeker_register.html', context)



# send email method to activate the user
def jobseeker_activate(email, token):
    mail_subject = 'Activate your account.'
    message = f'Please click on the link to confirm your registration, http://127.0.0.1:8000/jobseeker-verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    list = [email]
    send_mail(mail_subject, message, email_from, list)




# to verify your user account
def jobseeker_verify(request, token):
    try:
        jobseeker_object = Jobseeker.objects.filter(token=token).first()
        if jobseeker_object:
            jobseeker_object.is_jobseeker = True
            jobseeker_object.save()
            
            return redirect('jobseeker_login')
        else:
            return render(request, 'accounts/jobseeker_register.html')

    except Exception as e:
        print(e)

#jobseeker login page
def jobseeker_login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.add_message(request, messages.WARNING, 'You have not been register yet!' )

        joseeker_profile = Jobseeker.objects.filter(user = user_obj).first()
        if joseeker_profile.is_jobseeker == False:
            messages.add_message(request, messages.WARNING, 'Please check your email to verify!' )

        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # print (username)
            if user.jobseeker.is_jobseeker:
                # print(password)
                loggedin(request, user)
                return redirect('jobseeker_profile')
        else:
            messages.add_message(request, messages.ERROR, 'Incorrect Username or Password!')
    except Exception as e:
        print(e)

    return render(request, 'accounts/jobseeker_login.html')

#employer registration
# create object of user and employer
#  send email 
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
                user_form.is_active = False
                email = request.POST.get('email')
                # print(email)
                user_form.save()

                industry_type = request.POST.get('industry_type')
                # print(industry_type)
                
                token = str(uuid.uuid4())

                # print(token)
                employer_profile = Employer.objects.create(user=user_form.instance, token = token, industry_type=industry_type)
                employer_profile.save()

                employer_activate(email, token)
                messages.add_message(request, messages.INFO, 'Please check your email to verify your Account!')
                return redirect('login')
            else:
                messages.add_message(request, messages.ERROR, 'This username is already taken!')
    except Exception as e:
        print(e)

    
    return render(request, 'accounts/employer_register.html', context)

#send an activation email
def employer_activate(email, token):
    mail_subject = 'Activate your account.'
    message = f'Please click on the link to confirm your registration, http://127.0.0.1:8000/employer-verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    list = [email]
    send_mail(mail_subject, message, email_from, list)

#to verify email account 
def employer_verify(request, token):
    try:
        employer_object = Employer.objects.filter(token=token).first()
        if employer_object:
            employer_object.is_employer = True
            employer_object.save()
            print('Your account is verified')
            return redirect('employer_login')
        else:
            return redirect('employer_register')

    except Exception as e:
        print(e)

# employer login
# get value of username and password
# check the user with username fields
# check the user, and if the user is authenticated user is verified as employer 
# sends user to employer page
def employer_login(request):

    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.add_message(request, messages.ERROR, 'You have not been register yet!')

        employer_profile = Employer.objects.filter(user = user_obj).first()
        if employer_profile.is_employer == False:
            messages.add_message(request, messages.WARNING, 'Please check your email to verify!' )

        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print (username)
            if user.employer.is_employer:
                
                loggedin(request, user)
                return redirect('employer_profile')
        else:
            messages.add_message(request, messages.ERROR, 'Incorrect Username or Password!')
    except Exception as e:
        print(e)

    return render(request, 'accounts/employer_login.html')


# change password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.add_message(request, messages.ERROR, 'Incorrect Username or Password!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

    