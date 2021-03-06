from django.db import models
from django.contrib.auth.models import User
from accounts.models import Jobseeker, Employer

class Jobseeker_profile(models.Model):
    jobseeker_user = models.OneToOneField(Jobseeker, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')