from django.urls import path

from map import views

urlpatterns = [
    path('', views.MapView.as_view(), name='map'),
    path('change-location', views.EditLocationView.as_view(), name='change-location'),
    path('add-location', views.AddLocationView.as_view(), name='add-location'),
    path('delete-location', views.DeleteLocationView.as_view(), name='delete-location'),
]
