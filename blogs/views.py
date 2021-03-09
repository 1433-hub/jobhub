from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blogs.forms import UserUpdateForm, JobseekerUpdateForm, JobseekerProfileUpdateForm, JobseekerSkillUpdateForm, JobseekerLanguageUpdateForm, JobseekerEducationUpdateForm, JobseekerEmploymentUpdateForm
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

# employer profile page
@login_required
def employer_profile(request):
    return render(request, 'users-profile/employer_profile.html')

# jobseeker profile page    
@login_required
def jobseeker_profile(request):
    return render(request, 'users-profile/jobseeker_profile.html')


# jobseeker profile update 
def jobseeker_profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, 
                                    instance=request.user)
        jobseeker_form = JobseekerUpdateForm(request.POST, 
                                            instance=request.user.jobseeker)
        jobseeker_profile_form = JobseekerProfileUpdateForm(request.POST, 
                                                            request.FILES, 
                                                            instance=request.user.jobseeker.jobseeker_profile)
        if user_form.is_valid() and jobseeker_form.is_valid() and jobseeker_profile_form.is_valid():
            user_form.save()
            jobseeker_form.save()
            jobseeker_profile_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your account has been updated!') 
            return redirect('jobseeker_profile')                                          
    else:
        user_form = UserUpdateForm(instance=request.user)
        jobseeker_form = JobseekerUpdateForm(instance=request.user.jobseeker)
        jobseeker_profile_form = JobseekerProfileUpdateForm(instance=request.user.jobseeker.jobseeker_profile)
        context = {
            'user_form': user_form,
            'jobseeker_form': jobseeker_form,
            'jobseeker_profile_form': jobseeker_profile_form
        }
    return render(request, 'users-profile/jobseeker_profile_update.html', context)


# update skill
def jobseeker_skill_update(request):
    
    skill = JobseekerSkillUpdateForm()
    if request.method == 'POST':
        skill = JobseekerSkillUpdateForm(request.POST, instance=request.user.jobseeker.skill)
        if skill.is_valid():
            skill.save()
            messages.add_message(request, messages.SUCCESS, 'Your Skill has been updated!') 
            return redirect('jobseeker_profile')
        else:
            return render(request, 'users-profile/jobseeker_skill_update.html', {'jobseeker_skill': skill})
    else:
        return render(request, 'users-profile/jobseeker_skill_update.html', {'jobseeker_skill': skill})


def jobseeker_language_update(request):
    
    language = JobseekerLanguageUpdateForm()
    if request.method == 'POST':
        language = JobseekerLanguageUpdateForm(request.POST, instance=request.user.jobseeker.language)
        if language.is_valid():
            language.save()
            messages.add_message(request, messages.SUCCESS, 'Your Skill has been updated!')
            return redirect('jobseeker_profile')
        else:
            return render(request, 'users-profile/jobseeker_language_update.html', {'jobseeker_language': language})
    else:
        return render(request, 'users-profile/jobseeker_language_update.html', {'jobseeker_language': language})


def jobseeker_education_update(request):
    education = JobseekerEducationUpdateForm()
    if request.method == 'POST':
        education = JobseekerEducationUpdateForm(request.POST, instance=request.user.jobseeker.education)
        if education.is_valid():
            education.save()
            messages.add_message(request, messages.SUCCESS, 'Your Education has been updated!')
            return redirect('jobseeker_profile')
        else:
             return render(request, 'users-profile/jobseeker_education_update.html', {'jobseeker_education': education})
    return render(request, 'users-profile/jobseeker_education_update.html', {'jobseeker_education': education})


def jobseeker_employment_update(request):
    employment = JobseekerEmploymentUpdateForm()
    if request.method == 'POST':
        employment = JobseekerEmploymentUpdateForm(request.POST, instance=request.user.jobseeker.employment)
        if employment.is_valid():
            employment.save()
            messages.add_message(request, messages.SUCCESS, 'Your Education has been updated!')
            return redirect('jobseeker_profile')
    return render(request, 'users-profile/jobseeker_employment_update.html', {'jobseeker_employment': employment})