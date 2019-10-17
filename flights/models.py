from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Flight(models.Model):
    # customer = models.ForeignKey('auth.User', related_name='flights', on_delete=models.CASCADE)

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
        return self.departure_location