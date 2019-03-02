from django.shortcuts import render
from django.views.generic import ListView
from map import models


class MapView(ListView):
    model = models.FriendLocation
    context_object_name = 'locations'
    template_name = 'map/map.html'
