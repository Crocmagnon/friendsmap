from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Friend

admin.site.register(Friend, UserAdmin)
