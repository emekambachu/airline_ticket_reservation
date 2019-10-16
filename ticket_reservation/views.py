from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'

class ProfilePage(TemplateView):
    template_name = 'accounts/profile.html'

class LogoutPage(TemplateView):
    template_name = 'accounts/login.html'