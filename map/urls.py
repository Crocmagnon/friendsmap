from django.urls import path

from map import views

urlpatterns = [
    path('', views.MapView.as_view(), name='map'),
    path('change-location/<int:pk>', views.EditLocationView.as_view(), name='change-location'),
    path('add-location/<int:pk>', views.AddLocationView.as_view(), name='add-location'),
]
