from django.contrib import admin

# Register your models here.

from jingle.models import Category, UserProfile

admin.site.register(Category)
admin.site.register(UserProfile)
