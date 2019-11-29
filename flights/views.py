from django.shortcuts import render, get_object_or_404, redirect

from django.db import IntegrityError

from django.contrib import messages

# run pip install django-braces first
from braces.views import SelectRelatedMixin

from . models import Flight, Reservation

from . forms import CreateFlightForm

from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView)

# import for django mail
from django.core.mail import send_mail

# import html email string loader
from django.template.loader import render_to_string

# import strip tags
from django.utils.html import strip_tags

# import django settings
from django.conf import settings

# get logged in user details for this view
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


class AllFlightsView(ListView):
    model = Flight


class CreateFlightView(LoginRequiredMixin, CreateView):

    form_class = CreateFlightForm
    model = Flight
    redirect_field_name = 'flights/flight_detail.html'


class FlightDetailView(DetailView):
    model = Flight


class FlightUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'flights/flight_detail.html'
    # form_class = FlightUpdateForm
    model = Flight


class FlightDeleteView(LoginRequiredMixin, DeleteView):
    model = Flight
    success_url = reverse_lazy('flights:all-flights')


class AllReservationsView(LoginRequiredMixin, ListView):
    model = Flight
    select_related = ('user', 'flight')


class BookTicket(LoginRequiredMixin, RedirectView):

    # redirect to flight detail after booking
    def get_redirect_url(self, *args, **kwargs):
        return reverse('flights:flight-detail', kwargs={'pk': self.kwargs.get('pk')})

    # give an error if flight has been booked by user
    def get(self, request, *args, **kwargs):
        flight = get_object_or_404(Flight, pk=self.kwargs.get('pk'))

        try:
            # create object for reservation where user is equal to logged in or current user
            reservation = Reservation.objects.create(user=self.request.user, flight=flight)
            customer = self.request.user
        except IntegrityError:
            messages.warning(self.request, 'Warning! Already a booked')
        else:
            # send email
            subject = "Ticket " + reservation.reservation_code + " has been booked"
            html_message = render_to_string('flights/reservation_template.html', {
                'firstname': customer.first_name,
                'lastname': customer.last_name,
                'username': customer.username,
                'email': customer.email,
                'ticket': reservation.reservation_code,
                'from': flight.departure_location,
                'from_date': flight.departure_date,
                'to': flight.arrival_location,
                'to_date': flight.arrival_date,
                'subject': subject
            })
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to = customer.email

            send_mail(subject, plain_message, from_email, [to, 'xeddtech@gmail.com'], html_message=html_message)
            messages.success(self.request, 'Your Ticket has been reserved')

        return super().get(request, *args, **kwargs)


class CancelTicket(LoginRequiredMixin, RedirectView):
    pass