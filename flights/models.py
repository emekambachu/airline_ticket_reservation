from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Flight(models.Model):
    customer = models.ForeignKey('auth.User', related_name='flights', on_delete=models.CASCADE)
    departure_location = models.CharField(max_length=200)
    departure_time = models.CharField(max_length=200)
    arrival_location = models.CharField(max_length=200)
    arrival_time = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("flights:flight_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.departure_location