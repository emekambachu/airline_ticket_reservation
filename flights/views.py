from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.


class AllFlightsView(TemplateView):
    template_name = 'flights/all_flights.html'


class CreateFlightView(TemplateView):
    template_name = 'flights/create_flight.html'