from accounts.models import Jobseeker, Employer
from blogs.models import Employer_profile, Jobseeker_profile, Skill, Language, Education, Employment
from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class EmployerUpdateForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['industry_type', 'company_name']

class EmployerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Employer_profile
        fields = ['image', 'phone_number']

class JobseekerUpdateForm(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = ['job_category', 'gender']

class JobseekerProfileUpdateForm(forms.ModelForm):
    phone_number = forms.IntegerField(required=True)
    date_of_birth = forms.DateField(required=True)
    class Meta:
        model = Jobseeker_profile
        fields = ['image','phone_number', 'date_of_birth']

class JobseekerSkillUpdateForm(forms.ModelForm):
    SKILL_CHOICE = (
        ('Select One', 'Select One'),
        ('Web Development', 'Web Development'),
        ('Communication', 'Communication'),
        ('Marketing', 'Marketing'),
        ('Photoshop', 'Photoshop'),
        ('Php', 'Php'),
        ('Accounting', 'Accounting'),
        ('Css', 'Css'),
        ('Data Analysis', 'Data Analysis'),
    )
    skill = forms.ChoiceField(choices=SKILL_CHOICE)
    class Meta:
        model = Skill
        fields = ['skill']

class JobseekerLanguageUpdateForm(forms.ModelForm):
    LANGUAGE_CHOICE = (
        ('Select One', 'Select One'),
        ('English', 'English'),
        ('Nepali', 'Nepali'),
        ('Hindi', 'Hindi'),
        ('Korean', 'Korean'),
        ('Japanese', 'Japanese'),
    )
    language = forms.ChoiceField(choices=LANGUAGE_CHOICE)
    class Meta:
        model = Language
        fields = ['language']

class JobseekerEducationUpdateForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school_name', 'high_school', 'degree', 'start_date', 'end_date', 'description']

class JobseekerEmploymentUpdateForm(forms.ModelForm):
    class Meta:
        model = Employment
        fields = ['company_name', 'designation', 'title', 'start_date', 'end_date', 'description']
