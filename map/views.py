from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from map import models
from map.mixins import QuickActionsMixin


class MapView(LoginRequiredMixin, QuickActionsMixin, generic.ListView):
    model = models.FriendLocation
    context_object_name = 'locations'
    template_name = 'map/map.html'

    def get_quick_actions(self):
        return [
            {
                'url': reverse_lazy('change-location', kwargs={'pk': self.request.user.location.pk}),
                'category': 'secondary',
                'display': f'Change your location'
            },
        ]


class EditLocationView(LoginRequiredMixin, generic.UpdateView):
    model = models.FriendLocation
    context_object_name = 'location'
    template_name = 'map/change_location.html'

    fields = [
        'latitude',
        'longitude',
        'start_date',
        'end_date',
    ]

    success_url = reverse_lazy('map')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()  # type: models.FriendLocation
        if obj is None or obj.friend != request.user:
            messages.warning(request, "This is not your location.")
            return redirect('map')

        return super().dispatch(request, *args, **kwargs)
