from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'accounts/login.html'


class LogoutPage(TemplateView):
    template_name = 'home.html'