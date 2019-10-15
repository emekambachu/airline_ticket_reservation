from django.contrib import admin
from . models import Profile

# Register your models here.
admin.site.register(Profile)


class Profile(admin.ModelAdmin):
    list_display = ('role', 'first_name', 'last_name')