from django.db.models.signals import post_save
from accounts.models import Jobseeker, Employer
from django.dispatch import receiver
from .models import Jobseeker_profile, Employer_profile
from django.contrib.auth.models import User

#receive a signals from user 
#create a jobseeker profile
@receiver(post_save, sender=Jobseeker)
def create_jobseeker_profile(sender, instance, created, **kwargs):
    if created:
        Jobseeker_profile.objects.create(jobseeker_user=instance)


#save jobseeker profile in db
@receiver(post_save, sender=Jobseeker)
def save_jobseeker_profile(sender, instance, **kwargs):
    instance.jobseeker_profile.save()


#create a jobseeker profile
@receiver(post_save, sender=Employer)
def create_employer_profile(sender, instance, created, **kwargs):
    if created:
        Employer_profile.objects.create(employer_user=instance)




#save employer profile in db
@receiver(post_save, sender=Employer)
def save_employer_profile(sender, instance, **kwargs):
    instance.employer_profile.save()






#create a employer profile
@receiver(post_save, sender=Employer)
def create_employer_profile(sender, instance, created, **kwargs):
    if created:
        Employer_profile.objects.create(employer_user=instance)


#save employer profile in db
@receiver(post_save, sender=Employer)
def save_employer_profile(sender, instance, **kwargs):
    instance.employer_profile.save()