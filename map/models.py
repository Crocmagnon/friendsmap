from django.contrib.auth.models import AbstractUser
from django.db import models

from map.fields import CoordinateField


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Friend(AbstractUser):
    def get_display_name(self):
        display_name = super().get_full_name()
        if not display_name:
            display_name = self.username

        return display_name


class FriendLocation(BaseModel):
    latitude = CoordinateField()
    longitude = CoordinateField()
    start_date = models.DateField('from', blank=True, null=True)
    end_date = models.DateField('until', blank=True, null=True)
    friend = models.OneToOneField(Friend, on_delete=models.CASCADE, related_name='location')

    @property
    def latitude_str(self):
        return str(self.latitude)

    @property
    def longitude_str(self):
        return str(self.longitude)

    def __str__(self):
        result = f'{self.friend.get_display_name()}'
        if self.start_date:
            result += f' from {self.start_date}'
        if self.end_date:
            result += f' until {self.end_date}'
        return result

    @property
    def safe_html(self):
        html = f'<strong>{self.friend.get_display_name()}</strong>'
        if self.start_date:
            html += f' from {self.start_date}'
        if self.end_date:
            html += f' until {self.end_date}'
        return html

