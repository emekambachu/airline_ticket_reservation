from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone

from . models import Flight

from . forms import CreateFlightForm

from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.


class AllFlightsView(ListView, LoginRequiredMixin):
    model = Flight


class CreateFlightView(CreateView, LoginRequiredMixin):
    form_class = CreateFlightForm
    model = Flight


class FlightUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'flights/flight_detail.html'
    # form_class = FlightUpdateForm
    model = Flight


class FlightDeleteView(LoginRequiredMixin, DeleteView):
    model = Flight
    success_url = reverse_lazy('flights:all-flights')