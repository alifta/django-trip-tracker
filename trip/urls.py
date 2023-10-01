from django.urls import path

from .views import (
    HomeView,
    NoteCreateView,
    NoteDeleteView,
    NoteDetailView,
    NoteListView,
    NoteUpdateView,
    TripCreateView,
    TripDetailView,
    trip_list,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", trip_list, name="trip-list"),
    path("dashboard/note/", NoteListView.as_view(), name="note-list"),
    path("dashboard/note/create/", NoteCreateView.as_view(), name="note-create"),
    path("dashboard/trip/create/", TripCreateView.as_view(), name="trip-create"),
    path("dashboard/trip/<int:pk>/", TripDetailView.as_view(), name="trip-detail"),
    path("dashboard/note/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
    path("dashboard/note/<int:pk>/update/", NoteUpdateView.as_view(), name="note-update"),
    path("dashboard/note/<int:pk>/delete/", NoteDeleteView.as_view(), name="note-delete"),
]
