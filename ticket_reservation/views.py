from django.views.generic import TemplateView, View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from flights.models import Flight, Reservation

# get logged in user details for this view
from django.contrib.auth import get_user_model
User = get_user_model()


class HomePage(ListView):
    template_name = 'home.html'
    model = Flight


class ProfilePage(LoginRequiredMixin, ListView):
    template_name = 'accounts/profile.html'
    model = Flight
    select_related = ('user', 'flight')

    # for multiple models in a template
    # def get_context_data(self, **kwargs):
    #     context = super(ProfilePage, self).get_context_data(**kwargs)
    #     context['reservations'] = Reservation.objects.all()
    #     context['flights'] = Flight.objects.all()
    #     # And so on for more models
    #     return context


class LogoutPage(TemplateView):
    template_name = 'accounts/login.html'