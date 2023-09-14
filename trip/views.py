from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

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
