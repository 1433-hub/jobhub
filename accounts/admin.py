from django.contrib import admin
from .models import User, Jobseeker, Employer

admin.site.register(User)
admin.site.register(Jobseeker)
admin.site.register(Employer)
