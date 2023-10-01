from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Trip, Note


# Create your views here.
class HomeView(TemplateView):
    template_name = "trip/index.html"


def trip_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {"trips": trips}
    return render(request, "trip/trip_list.html", context)


class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy("trip-list")
    fields = ["city", "country", "start_date", "end_date"]
    # Template file is mode_form.html i.e. trip_form.html

    # Overriding the form_valid function which gets triggered
    # Every time the form get submitted to create a new trip
    def form_valid(self, form):
        # We want owner be equal to logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TripDetailView(DetailView):
    model = Trip

    # Data stored on Trip, but we also have the Notes data
    # So we can override the following function
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context["object"]
        notes = trip.notes.all()
        context["notes"] = notes
        return context


class NoteDetailView(DetailView):
    model = Note


class NoteListView(ListView):
    model = Note

    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset


class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy("note-list")
    fields = "__all__"

    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form
    

class NoteUpdateView(UpdateView):
    model = Note
    success_url = reverse_lazy("note-list")
    fields = "__all__"

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form

class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy("note-list")
