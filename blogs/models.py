from django.db import models
from django.contrib.auth.models import User
from accounts.models import Jobseeker, Employer


# basic information of jobseeker
class Jobseeker_profile(models.Model):
    jobseeker_user = models.OneToOneField(Jobseeker, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    phone_number = models.PositiveBigIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.jobseeker_user.user.username
# education table of jobseeker
class Jobseeker_education(models.Model):
    jobseeker_user = models.OneToOneField(Jobseeker, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=150, blank=True, null=True)
    high_school = models.CharField(max_length=150, blank=True, null=True)
    degree = models.CharField(max_length=150, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.jobseeker_user.user.username


# language table of jobseeker
class Jobseeker_language(models.Model):
    LANGUAGE_CHOICE = (
        ('English', 'English'),
        ('Nepali', 'Nepali'),
        ('Hindi', 'Hindi'),
        ('Korean', 'Korean'),
        ('Japanese', 'Japanese'),
    )
    jobseeker_user = models.OneToOneField(Jobseeker, on_delete=models.CASCADE)
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICE)

    def __str__(self):
        return self.jobseeker_user.user.username

# skill table of jobseeker
class Jobseeker_skill(models.Model):
    SKILL_CHOICE = (
        ('Web Development', 'Web Development'),
        ('Communication', 'Communication'),
        ('Marketing', 'Marketing'),
        ('Photoshop', 'Photoshop'),
        ('Php', 'Php'),
        ('Accounting', 'Accounting'),
        ('Css', 'Css'),
        ('Data Analysis', 'Data Analysis'),
    )
    jobseeker_user = models.OneToOneField(Jobseeker, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100, choices=SKILL_CHOICE)

    def __str__(self):
        return self.jobseeker_user.user.username


# employment table of jobseeker
class Jobseeker_employment(models.Model):
    jobseeker_user = models.OneToOneField(Jobseeker, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    designation = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.jobseeker_user.user.username



class Employer_profile(models.Model):
    employer_user = models.OneToOneField(Employer, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    phone_number = models.PositiveBigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.employer_user.user.username