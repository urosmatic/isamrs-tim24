from django.shortcuts import render
from django.http import HttpResponse
from .models import Airline, Destination
from django.views.generic import ListView
# Create your views here.


def home(request):
    """View function for home page of site."""
    return render(request,'flightsbooking/home.html')

class AirlineListView(ListView):
    model = Airline
    template_name = 'flightsbooking/home.html'
    context_object_name = 'airlines'

