from django.contrib.auth.models import AbstractUser
from django.db import models

from map.fields import CoordinateField


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Friend(AbstractUser):
    pass


class FriendLocation(BaseModel):
    latitude = CoordinateField()
    longitude = CoordinateField()
    start_date = models.DateField('from', blank=True, null=True)
    end_date = models.DateField('until', blank=True, null=True)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)

    @property
    def latitude_str(self):
        return str(self.latitude)

    @property
    def longitude_str(self):
        return str(self.longitude)

    def __str__(self):
        return f'{self.friend.get_full_name()} from {self.start_date} to {self.end_date}'

