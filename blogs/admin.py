from django.contrib import admin
from .models import Jobseeker_profile, Jobseeker_skill, Jobseeker_language, Jobseeker_education, Jobseeker_employment, Employer_profile


admin.site.register(Jobseeker_profile)
admin.site.register(Jobseeker_skill)
admin.site.register(Jobseeker_language)
admin.site.register(Jobseeker_education)
admin.site.register(Jobseeker_employment)
admin.site.register(Employer_profile)
