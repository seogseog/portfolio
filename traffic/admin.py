from django.contrib import admin
from .models import *


class TrafficAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(TrafficDB, TrafficAdmin)
