# dishes/admin.py

from django.contrib import admin
# REMOVED: from django.db import models # This line was incorrect and caused the AttributeError
# Import both the Dishes and Drink models
from .models import Category, Dishes, Drink # Importing our Category, Dishes, and Drink models.

# Registering our models so they appear in the Django admin interface.
# This makes Category, Dishes, and Drink manageable.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Displays only the 'name' in the admin list view for Category objects.
    list_display = ('name',)
    # Enables searching by category name in the admin.
    search_fields = ('name',)

@admin.register(Dishes) # Registering the Dishes model
class DishesAdmin(admin.ModelAdmin): # Admin class name for Dishes
    # Customizes which fields are displayed in the list of dishes in the admin.
    # Removed 'ingredients' and 'instructions' from here as requested.
    list_display = ('title', 'category', 'status', 'created_on', 'author')
    # Enables searching by title and description for dishes.
    # Removed 'ingredients' and 'instructions' from here as requested.
    search_fields = ('title', 'description')
    # Adds filters to the sidebar to filter dishes by status, creation date, and category.
    list_filter = ('status', 'created_on', 'category')
    # This is very handy! When a title is entered, the slug field will automatically populate.
    # This saves typing and helps with SEO-friendly URLs.
    prepopulated_fields = {'slug': ('title',)}
    # Adds a date hierarchy to browse dishes by year, month, and day.
    date_hierarchy = 'created_on'

# NEW: Registering the Drink model
@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin): # Admin class for Drink (ModelAdmin is from django.contrib.admin)
    # Customizes the fields displayed in the admin list view for Drink objects
    list_display = ('title', 'category', 'status', 'created_on', 'author')
    # Enables searching by title and description for drinks
    search_fields = ('title', 'description')
    # Adds filters for status, creation date, and category for drinks
    list_filter = ('status', 'created_on', 'category')
    # Automatically populates the slug field from the title for drinks
    prepopulated_fields = {'slug': ('title',)}
    # Adds a date hierarchy for drinks
    date_hierarchy = 'created_on'