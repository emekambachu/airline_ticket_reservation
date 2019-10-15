from django.shortcuts import render

# import for redirection after successful submission
from django.urls import reverse_lazy

# import for generic class based views
from django.views.generic import CreateView

# import forms
from . import forms

# Create your views here.
class UserSignUpPage(CreateView):

    # add form class from forms.py
    form_class = forms.UserSignupForm

    # after a successful sign up go to login page
    success_url = reverse_lazy('login')

    # add template name for signup
    template_name = 'accounts/signup.html'