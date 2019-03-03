from django.urls import path

from map import views

urlpatterns = [
    path('', views.MapView.as_view(), name='map'),
    path('change-location', views.EditLocationView.as_view(), name='change-location'),
    path('add-location', views.AddLocationView.as_view(), name='add-location'),
    path('delete-location', views.DeleteLocationView.as_view(), name='delete-location'),
    path('share-location', views.LocationSharingView.as_view(), name='share-location'),
    path('accounts/profile', views.UpdateProfileView.as_view(), name='change-profile'),
    path('accounts/profile/delete', views.DeleteProfileView.as_view(), name='delete-profile'),
]
