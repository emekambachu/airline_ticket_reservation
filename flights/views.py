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
    model = Reservation


class ReservationDetailView(LoginRequiredMixin, TemplateView):
    model = Reservation
    template_name = 'flights/reservation_detail.html'


class BookTicket(LoginRequiredMixin, RedirectView):

    # redirect to flight detail after booking
    def get_redirect_url(self, *args, **kwargs):
        return reverse('flights:reservation-detail', kwargs={'pk': self.kwargs.get('pk')})

    # give an error if flight has been booked by user
    def get(self, request, *args, **kwargs):
        flight = get_object_or_404(Flight, pk=self.kwargs.get('pk'))

        try:
            # create object for reservation where user is equal to logged in or current user
            Reservation.objects.create(user=self.request.user, flight=flight)
        except IntegrityError:
            messages.warning(self.request, 'Warning! Already a booked')
        else:
            messages.success(self.request, 'Your Ticket has been reserved')

        return super().get(request, *args, **kwargs)


class CancelTicket(LoginRequiredMixin, RedirectView):
    pass