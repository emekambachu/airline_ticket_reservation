from django.shortcuts import render, get_object_or_404, redirect

from . models import Flight

from . forms import CreateFlightForm

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

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