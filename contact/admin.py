
from django.contrib import admin
from .models import *


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id','name','slug']
#     prepopulated_fields = {'slug':['name']}
#
#
# admin.site.register(Category,CategoryAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','email','phone','message']
    list_filter = ['firstname','lastname','created','updated']


admin.site.register(Contact, ContactAdmin)