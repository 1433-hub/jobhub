from django.db.models.signals import post_save
from accounts.models import Jobseeker, Employer
from django.dispatch import receiver
from .models import Jobseeker_profile, Employer_profile, Skill, Language, Education, Employment
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





#create a object jobseeker user 
@receiver(post_save, sender=Jobseeker)
def create_skill(sender, instance, created, **kwargs):
    if created:
        Skill.objects.create(jobseeker_user=instance)


#save jobseeker user in skill db
@receiver(post_save, sender=Jobseeker)
def save_skill(sender, instance, **kwargs):
    instance.skill.save()





#create a object jobseeker user 
@receiver(post_save, sender=Jobseeker)
def create_language(sender, instance, created, **kwargs):
    if created:
        Language.objects.create(jobseeker_user=instance)


#save jobseeker user in language db
@receiver(post_save, sender=Jobseeker)
def save_language(sender, instance, **kwargs):
    instance.language.save()





#create a object jobseeker user 
@receiver(post_save, sender=Jobseeker)
def create_education(sender, instance, created, **kwargs):
    if created:
        Education.objects.create(jobseeker_user=instance)


#save jobseeker user in education db
@receiver(post_save, sender=Jobseeker)
def save_education(sender, instance, **kwargs):
    instance.education.save()





#create a object jobseeker user 
@receiver(post_save, sender=Jobseeker)
def create_employment(sender, instance, created, **kwargs):
    if created:
        Employment.objects.create(jobseeker_user=instance)


#save jobseeker user in skill db
@receiver(post_save, sender=Jobseeker)
def save_employment(sender, instance, **kwargs):
    instance.employment.save()






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