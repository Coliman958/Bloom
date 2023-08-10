from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm, ChangeProfileForm, CreateProfileForm, EditProfilePageForm
from django.views.generic import DetailView, UpdateView, CreateView
from Bromine.models import Profile


class DisplayProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        
        context = super(DisplayProfileView, self).get_context_data(*args, **kwargs)
        this_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['this_user'] = this_user
        return context
    
    
class EditProfileView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    #fields = ['bio', 'profile_photo', 'twitter_url', 'facebook_url']
    form_class = EditProfilePageForm
    success_url = reverse_lazy('home')


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'registration/create_profile.html'
    form_class = CreateProfileForm
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    
    
    
    

class ProfileSettingsView(generic.UpdateView): # Here we used the UpdateView class
    form_class = ChangeProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):      # This helps the edit profile page to get the correct data
        return self.request.user