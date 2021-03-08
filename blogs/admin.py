from django.contrib import admin
from .models import Jobseeker_profile, Skill, Language, Education, Employment, Employer_profile


admin.site.register(Jobseeker_profile)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Education)
admin.site.register(Employment)


admin.site.register(Employer_profile)
