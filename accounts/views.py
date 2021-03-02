from django.shortcuts import render
from .forms import UserSignUpForm, EmployerSignUpForm
from .models import User, Employer

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def jobseeker_register(request):
    return render(request, 'accounts/jobseeker_register.html')

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
            # username = request.POST.get('username')
            # if User.objects.filter(username=username).first():
            #     print('username is taken')
            # email = request.POST.get('email')
            # if User.objects.filter(email=email).first():
            #     print('email is taken')

            if user_form.is_valid() and employer_form.is_valid():
                # email = user_form.cleaned_data.get('email')
                # print(email)

                user_form.save()
                phone_number = request.POST.get('phone_number')
                print(phone_number)
                
                # industry_type = request.POST.get('industry_type')
                employer_profile = Employer.objects.create(user=user_form.instance)
                employer_profile.save()

    except Exception as e:
        print(e)

    
    return render(request, 'accounts/employer_register.html', context)