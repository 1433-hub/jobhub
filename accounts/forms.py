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