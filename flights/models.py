from django.db import models
from django.utils import timezone
from django.urls import reverse
from accounts.models import Profile
from django.utils.crypto import get_random_string

# import current user model
from django.contrib.auth import get_user_model

from django import template

# connect current reservation to whichever user is logged in
User = get_user_model()

# use for connecting related name, import template from django first
register = template.Library()


# Create your models here.
class Flight(models.Model):
    departure_location = models.CharField(max_length=50, default=None, null=False)
    departure_date = models.DateField(max_length=50, default=None, null=False)
    departure_time = models.TimeField(max_length=50, default=None, null=False)
    arrival_location = models.CharField(max_length=50, default=None, null=False)
    arrival_date = models.DateField(max_length=50, default=None, null=False)
    arrival_time = models.TimeField(max_length=50, default=None, null=False)
    cost = models.IntegerField(default=0, null=False)
    customers = models.ManyToManyField(User, through='Reservation')
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("flights:flight-detail", kwargs={'pk': self.pk})

    def __str__(self):
        return "From " + self.departure_location + "to " + self.arrival_location + "at $" + str(self.cost)


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, related_name='reservations', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, default=0, related_name='user_flights', on_delete=models.CASCADE)
    reservation_code = models.CharField(default=0, null=False, max_length=20, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.reservation_code = "FLIGHT-" + get_random_string(12, '1234567890')
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('flight', 'user')

    def __str__(self):
        return str(self.reservation_code)