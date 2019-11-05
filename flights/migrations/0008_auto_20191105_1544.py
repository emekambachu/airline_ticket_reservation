# Generated by Django 2.2 on 2019-11-05 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0007_auto_20191105_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user_reservation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('flight', 'user')},
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='profile',
        ),
    ]
