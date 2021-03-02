from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_jobseeker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) 

class Jobseeker(models.Model):
    JOB_CATEGORY_TYPE = (
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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default='M')
    date_of_birth = models.DateField()
    phone_number = models.IntegerField(default=None)
    job_category = models.CharField(max_length=150, choices=JOB_CATEGORY_TYPE, default=None)

class Employer(models.Model):
    INDUSTRY_TYPE_CHOICE = (
        ('Manufacturing/Engineering','Manufacturing/Engineering'),
        ('Advertising Agency','Advertising Agency'),
        ('Banks','Banks'),
        ('Education','Education'),
        ('Information/Computer','Information/Computer'),
        ('Finances Companies','Finances Companies'),
        ('E-commerce/E-business','E-commerce/E-business'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=None)
    industry_type = models.CharField(max_length=150, choices=INDUSTRY_TYPE_CHOICE, default=None)