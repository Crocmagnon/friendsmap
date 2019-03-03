from django import forms

from map.models import FriendLocation, Friend


class LocationForm(forms.ModelForm):
    class Meta:
        model = FriendLocation
        fields = [
            'latitude',
            'longitude',
            'start_date',
            'end_date',
            'friend',
        ]
        widgets = {'friend': forms.HiddenInput()}

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_friend(self):
        return self.request.user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'shares_location_to',
        ]

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.fields['shares_location_to'].queryset = Friend.objects.exclude(pk=request.user.pk)
