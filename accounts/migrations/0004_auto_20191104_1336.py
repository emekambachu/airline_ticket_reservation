# Generated by Django 2.2 on 2019-11-04 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191015_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.AddField(
            model_name='profile',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
