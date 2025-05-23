from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm

from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

class CreateProfileView(CreateView):
    template_name='profiles/create_profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/profiles'

class ProfilesView(ListView):
    model = UserProfile
    template_name = 'profiles/user_profiles.html'
    context_object_name = 'profiles'
