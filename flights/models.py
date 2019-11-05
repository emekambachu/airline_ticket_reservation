from django.db import models
from django.utils import timezone
from django.urls import reverse
from accounts.models import Profile
from django.utils.crypto import get_random_string


# Create your models here.
class Flight(models.Model):
    departure_location = models.CharField(max_length=50, default=None, null=False)
    departure_date = models.DateField(max_length=50, default=None, null=False)
    departure_time = models.TimeField(max_length=50, default=None, null=False)
    arrival_location = models.CharField(max_length=50, default=None, null=False)
    arrival_date = models.DateField(max_length=50, default=None, null=False)
    arrival_time = models.TimeField(max_length=50, default=None, null=False)
    cost = models.IntegerField(default=0, null=False)
    status = models.IntegerField(default=1)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def create(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("flights:flight-detail", kwargs={'pk': self.pk})

    def __str__(self):
        return "From " + self.departure_location + "to " + self.arrival_location + "at $" + str(self.cost)


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, related_name='reservations', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name='user_reservation', on_delete=models.CASCADE)
    reservation_code = models.CharField(default=0, null=False)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.reservation_code = "FLIGHT" + get_random_string(12, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        super().save(*args, **kwargs)

    # Use this for url paths in url.py
    def get_absolute_url(self):
        return reverse('flights:reservation-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.reservation_code)