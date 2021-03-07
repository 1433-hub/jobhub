from django.contrib.auth.forms import UserCreationForm  
from .models import Jobseeker, Employer
from django import forms
from django.contrib.auth.models import User

class UserSignUpForm(UserCreationForm):  
    email = forms.EmailField()
    class Meta:  
        model = User
        fields = ( 'username', 'email', 'password1', 'password2')

class EmployerSignUpForm(forms.Form):
    INDUSTRY_TYPE_CHOICE = (
        ('Select One','Select One'),
        ('Manufacturing/Engineering','Manufacturing/Engineering'),
        ('Advertising Agency','Advertising Agency'),
        ('Banks','Banks'),
        ('Education','Education'),
        ('Information/Computer','Information/Computer'),
        ('Finances Companies','Finances Companies'),
        ('E-commerce/E-business','E-commerce/E-business'),
    )

    industry_type = forms.ChoiceField(choices=INDUSTRY_TYPE_CHOICE)
    class Meta:
        model = Employer
        fields = ('industry_type')


class JobseekerSignUpForm(forms.Form):
    JOB_CATEGORY_TYPE = (
        ('Select One','Select One'),
        ('Construction/Engineering','Construction/Engineering'),
        ('Create/Graphic','Create/Graphic'),
        ('Teaching/Education','Teaching/Education'),
        ('Hospitality','Hospitality'),
        ('Marketing/Advertising','Marketing/Advertising'),
        ('Accounting/Finance','Accounting/Finance'),
        ('IT & Communication','IT & Communication'),
    )
    GENDER_CHOICE = (
        ('M','Male'),
        ('F','Female'),
    )

    job_category = forms.ChoiceField(choices=JOB_CATEGORY_TYPE)
    gender = forms.ChoiceField(choices=GENDER_CHOICE)
    class Meta:
        model = Employer
        fields = ('gender', 'job_category')