# FriendsMap
FriendsMap is an open source project to let you share your location with your friends.

It's a "low tech" app in the sense that it doesn't use your phone or anything to retrieve your live location.
Instead, you can add the GPS coordinates you want to share directly in the app.
You can also add start and end dates, in order to indicate when you plan to get there or leave.

## Tech
FriendsMap uses [Django](https://www.djangoproject.com/) for the backend and the frontend rendering. No API or anything for the moment.

It also uses [Leaflet](https://leafletjs.com/) to display the map. The base map uses OpenStreetMap.

## Privacy
FriendsMap is built with privacy in mind :

- You're free to set the GPS coordinates to wherever you want,
in order not to disclose your real location in case the database were to be stolen.
- Your location is stored in the database but you choose who you send it to
- No Google Maps

There is still work to do though :
- Currently, the administrator can see everyone's location.
This is not a desirable thing but I have no idea how to improve this.
If you do, please let me know or propose a PR !

## Licenses
- The favicon is from Font Awesome under the Creative Commons Attribution 4.0 International license. It has
been transformed from svg to png. See [the licenses](https://fontawesome.com/license/free).
