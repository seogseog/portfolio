from django.contrib import admin

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'info', 'location', 'birth_date', 'gender']


admin.site.register(Profile, ProfileAdmin)
