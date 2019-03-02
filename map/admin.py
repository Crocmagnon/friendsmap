from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from .models import Friend, FriendLocation

admin.site.register(Friend, UserAdmin)


@register(FriendLocation)
class FriendLocationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('friend',)}),
        ('Place', {'fields': ('latitude', 'longitude')}),
        ('Dates', {'fields': ('start_date', 'end_date')}),
    ]
