from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from map import models


class MapView(LoginRequiredMixin, ListView):
    model = models.FriendLocation
    context_object_name = 'locations'
    template_name = 'map/map.html'
