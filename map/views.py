from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from map import models
from map.forms import LocationForm, LocationSharingForm
from map.mixins import QuickActionsMixin


class MapView(LoginRequiredMixin, QuickActionsMixin, generic.DetailView):
    model = models.Friend
    context_object_name = 'friend'
    template_name = 'map/map.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_quick_actions(self):
        if hasattr(self.request.user, 'location'):
            actions = [{
                'url': reverse_lazy('change-location'),
                'category': 'primary',
                'display': f'Change your location'
            }, {
                'url': reverse_lazy('delete-location'),
                'category': 'warning',
                'display': f'Delete your location'
            }]
        else:
            actions = [{
                'url': reverse_lazy('add-location'),
                'category': 'primary',
                'display': f'Add your location'
            }]

        actions.append({
            'url': reverse_lazy('share-location'),
            'category': 'secondary',
            'display': 'Share your location'
        })

        return actions


class EditLocationView(LoginRequiredMixin, QuickActionsMixin, generic.UpdateView):
    model = models.FriendLocation
    context_object_name = 'location'
    template_name = 'map/change_location.html'
    success_url = reverse_lazy('map')
    fields = [
        'latitude',
        'longitude',
        'start_date',
        'end_date',
    ]

    def get_quick_actions(self):
        return [{
            'url': reverse_lazy('map'),
            'category': 'secondary',
            'display': 'Back to map'
        }]

    def get_object(self, queryset=None):
        return self.request.user.location

    def get_success_url(self):
        messages.success(self.request, 'Your location has been successfully edited')
        return super().get_success_url()


class AddLocationView(LoginRequiredMixin, QuickActionsMixin, generic.CreateView):
    model = models.FriendLocation
    context_object_name = 'location'
    template_name = 'map/change_location.html'
    success_url = reverse_lazy('map')

    def get_quick_actions(self):
        return [{
            'url': reverse_lazy('map'),
            'category': 'secondary',
            'display': 'Back to map'
        }]

    def get_initial(self):
        initial = super().get_initial()
        initial = initial.copy()
        initial['friend'] = self.request.user
        return initial

    def get_form(self, form_class=None):
        return LocationForm(self.request, **self.get_form_kwargs())

    def get_success_url(self):
        messages.success(self.request, 'Your location has been successfully added')
        return super().get_success_url()


class DeleteLocationView(LoginRequiredMixin, generic.DeleteView):
    model = models.FriendLocation
    context_object_name = 'location'
    template_name = 'map/delete_location.html'
    success_url = reverse_lazy('map')

    def get_object(self, queryset=None):
        return self.request.user.location

    def get_success_url(self):
        messages.success(self.request, 'Your location has been successfully deleted')
        return super().get_success_url()


class UpdateProfileView(LoginRequiredMixin, QuickActionsMixin, generic.UpdateView):
    model = models.Friend
    context_object_name = 'friend'
    template_name = 'map/change_profile.html'
    success_url = reverse_lazy('map')
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
    ]

    def get_quick_actions(self):
        return [{
            'url': reverse_lazy('map'),
            'category': 'secondary',
            'display': 'Back to map'
        }]

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, 'Your profile has been successfully updated')
        return super().get_success_url()


class LocationSharingView(LoginRequiredMixin, QuickActionsMixin, generic.UpdateView):
    model = models.Friend
    context_object_name = 'friend'
    template_name = 'map/share_location.html'
    success_url = reverse_lazy('map')

    def get_quick_actions(self):
        return [{
            'url': reverse_lazy('map'),
            'category': 'secondary',
            'display': 'Back to map'
        }]

    def get_object(self, queryset=None):
        return self.request.user

    def get_form(self, form_class=None):
        return LocationSharingForm(self.request, **self.get_form_kwargs())


class DeleteProfileView(LoginRequiredMixin, generic.DeleteView):
    model = models.Friend
    context_object_name = 'friend'
    template_name = 'map/delete_profile.html'
    success_url = reverse_lazy('map')

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, 'Your profile has been successfully and permanently deleted')
        return super().get_success_url()
