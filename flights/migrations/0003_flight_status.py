# Generated by Django 2.2 on 2019-10-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_flight_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
