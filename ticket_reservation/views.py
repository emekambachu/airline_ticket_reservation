from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from flights.models import Flight, Reservation


class HomePage(TemplateView):
    template_name = 'home.html'


class ProfilePage(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.all()
        context['flights'] = Flight.objects.all()
        # And so on for more models
        return context


class LogoutPage(TemplateView):
    template_name = 'accounts/login.html'