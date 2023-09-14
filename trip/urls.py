from django.urls import path

from .views import HomeView, TripCreateView, trip_list

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", trip_list, name="trip-list"),
    path("dashboard/trip/create", TripCreateView.as_view(), name="trip-create"),
]
