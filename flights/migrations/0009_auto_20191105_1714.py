# Generated by Django 2.2 on 2019-11-05 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0008_auto_20191105_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='customers',
            field=models.ManyToManyField(through='flights.Reservation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_code',
            field=models.CharField(default=0, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user_flights', to=settings.AUTH_USER_MODEL),
        ),
    ]
