# dishes/views.py

from django.shortcuts import render
# Import your Dishes and Drink models to access the database
from .models import Dishes, Category, Drink # Imports our Dishes, Category, and Drink models.

def index(request):
    # Retrieve all published dishes from the database.
    # Order them by the newest first.
    dishes = Dishes.objects.filter(status=1).order_by('-created_on')
    
    # Retrieve all published drinks from the database.
    # Order them alphabetically by title.
    drinks = Drink.objects.filter(status=1).order_by('title')

    # Define a custom order for categories
    # based on user request: Appetizers, Main Courses, Desserts, then Drinks.
    # Mapping to existing category names in the database.
    custom_category_order_names = [
        "Main Course",
        "Soup",
        "Street Food", # Can be considered as a type of appetizer or light meal
        "Side Dish",
        "Snack", # Often served before or with meals
        "Dessert",
        "Beers",
        "Juices",
        "Soft Drinks",
    ]

    # Retrieve categories in the desired order
    ordered_categories = []
    for category_name in custom_category_order_names:
        try:
            category = Category.objects.get(name=category_name)
            ordered_categories.append(category)
        except Category.DoesNotExist:
            # Skips categories not found in the database.
            # This prevents errors if the list doesn't exactly match DB categories.
            pass

    # The context to be passed to the template.
    context = {
        'dishes': dishes,
        'drinks': drinks, # Adds drinks to the context.
        'categories': ordered_categories, # NEW: Adds categories in the custom order to the context.
    }
    
    # Renders the 'index.html' template and passes the context.
    return render(request, 'dishes/index.html', context)