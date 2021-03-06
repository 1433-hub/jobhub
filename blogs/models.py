from django.db import models
from django.contrib.auth.models import User
from accounts.models import Jobseeker, Employer

class Jobseeker_profile(models.Model):
    jobseeker_user = models.OneToOneField(Jobseeker, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.jobseeker_user.user.username

class Employer_profile(models.Model):
    employer_user = models.OneToOneField(Employer, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.employer_user.user.username