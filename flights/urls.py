from django.urls import path
from . import views


# Template Tagging
app_name = 'flights'

urlpatterns = [

    # class based views
    path('',
         views.AllFlightsView.as_view(),
         name='all-flights'),

    path('create-flight',
         views.CreateFlightView.as_view(),
         name='create-flight'),

    path('flight-detail/<int:pk>',
         views.FlightDetailView.as_view(),
         name='flight-detail'),

    path('all-reservations/',
         views.AllReservationsView.as_view(),
         name='all-reservations'),

    path('reservation-detail/<int:pk>',
         views.ReservationDetailView.as_view(),
         name='reservation-detail'),

    ]