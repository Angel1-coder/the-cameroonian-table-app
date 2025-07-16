# dishes/views.py

from django.shortcuts import render
# Import your Dishes and Drink models to access the database
from .models import Dishes, Category, Drink # Importing our Dishes, Category, and Drink models.

def index(request):
    # Retrieve all published dishes from the database.
    # Order them by the newest first.
    dishes = Dishes.objects.filter(status=1).order_by('-created_on')
    
    # Retrieve all published drinks from the database.
    # Order them alphabetically by title.
    drinks = Drink.objects.filter(status=1).order_by('title')

    # The context to be passed to the template.
    context = {
        'dishes': dishes,
        'drinks': drinks, # Add drinks to the context.
    }
    
    # Render the 'index.html' template and pass the context.
    return render(request, 'dishes/index.html', context)
