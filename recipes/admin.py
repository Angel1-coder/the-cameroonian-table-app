from django.contrib import admin

# recipes/admin.py

from django.contrib import admin
from .models import Category, Dish # Import our new Category and Dish models.

# Register your models here.
# This makes the Category and Dish models visible and manageable in the Django admin interface.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Displays the 'name' field in the admin list view for Category objects.
    list_display = ('name',)
    # Enables searching by the 'name' field in the admin.
    search_fields = ('name',)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    # Customizes the fields displayed in the admin list view for Dish objects.
    list_display = ('title', 'category', 'status', 'created_on', 'author')
    # Enables searching by 'title' and 'description' fields.
    search_fields = ('title', 'description')
    # Adds filters to the sidebar for 'status', 'created_on', and 'category'.
    list_filter = ('status', 'created_on', 'category')
    # Automatically populates the 'slug' field based on the 'title' input.
    prepopulated_fields = {'slug': ('title',)}
    # Adds a date-based drilldown navigation for 'created_on'.
    date_hierarchy = 'created_on'