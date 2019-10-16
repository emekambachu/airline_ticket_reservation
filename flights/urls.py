from django.urls import path
from . import views


# Template Tagging
app_name = 'flights'

urlpatterns = [

    # class based views
    path('all-flights',
         views.AllFlightsView.as_view(),
         name='all-flights'),

    path('create-flight',
         views.CreateFlightView.as_view(),
         name='create-flight'),
    ]