from django.shortcuts import render

# import for redirection after successful submission
from django.urls import reverse_lazy

# import for generic class based views
from django.views.generic import View, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

# from django.views.generic.edit import UpdateView

# import forms
from .forms import UserSignupForm

# import Profile class from model class
from .models import Profile

# import html email string loader
from django.template.loader import render_to_string

# import strip tags
from django.utils.html import strip_tags

# import django settings
from django.conf import settings

# import for django mail
from django.core.mail import send_mail

# get logged in user details for this view
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
class UserSignUpPage(View):
    model = Profile

    # add form class from forms.py
    form_class = UserSignupForm

    # after a successful sign up go to login page
    success_url = reverse_lazy('accounts:login')

    # add template name for signup
    template_name = 'accounts/signup.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            email = form.cleaned_data['email']

            user.set_password(password)
            user.save()

            # send email
            subject = "Account Created"
            html_message = render_to_string('mail_template.html', {
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'password': password,
                'email': email,
                'subject': subject
            })
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to = email

            send_mail(subject, plain_message, from_email, [to, 'xeddtech@gmail.com'], html_message=html_message)

        return render(request, self.template_name, {'form': form})


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'username']
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile
