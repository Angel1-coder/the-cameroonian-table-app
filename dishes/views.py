# dishes/views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # This view will later load the dishes from the database
    return HttpResponse("Welcome to The Cameroonian Table!") # Angepasst an den Restaurantnamen
