# dishes/admin.py

from django.contrib import admin
# Import both the Dishes and Drink models
from .models import Category, Dishes, Drink # Importing Dishes, Category, and Drink models

# Registering models so they appear in the Django admin interface.
# This makes Category, Dishes, and Drink manageable.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Displays just the 'name' in the admin list view for Category objects.
    list_display = ('name',)
    # Allows searching for categories by their name in the admin.
    search_fields = ('name',)

@admin.register(Dishes) # Registering the Dishes model
class DishesAdmin(admin.ModelAdmin): # Admin class name for Dishes
    # Customizes which fields are displayed in the list of dishes in the admin.
    # Added 'price' to list_display
    list_display = ('title', 'category', 'status', 'created_on', 'author', 'price')
    # Allows searching for dishes by their title, description, ingredients, and instructions.
    search_fields = ('title', 'description', 'ingredients', 'instructions')
    # Adds filters to the sidebar to filter dishes by status, creation date, and category.
    list_filter = ('status', 'created_on', 'category')
    # Automatically populates the slug field when a title is typed.
    prepopulated_fields = {'slug': ('title',)}
    # Adds a date hierarchy to browse dishes by year, month, and day.
    date_hierarchy = 'created_on'

    # --- Custom Admin Actions for Dishes ---
    # Defines a custom action to set selected dishes to 'Published' status.
    def change_status_to_published(self, request, queryset):
        queryset.update(status=1) # Update the 'status' field to 1 (Published).
        self.message_user(request, "Selected dishes successfully marked as Published.")
    # The display name in the admin action dropdown.
    change_status_to_published.short_description = "Mark selected dishes as Published" 

    # Defines a custom action to set selected dishes to 'Draft' status.
    def change_status_to_draft(self, request, queryset):
        queryset.update(status=0) # Update the 'status' field to 0 (Draft).
        self.message_user(request, "Selected dishes successfully marked as Draft.")
    # The display name in the admin action dropdown.
    change_status_to_draft.short_description = "Mark selected dishes as Draft" 

    # List of custom actions to be displayed in the admin dropdown.
    actions = ['change_status_to_published', 'change_status_to_draft']


# Registering the Drink model
@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    # Customize fields displayed in the admin list view for Drink objects
    # Added 'price' to list_display
    list_display = ('title', 'category', 'status', 'created_on', 'author', 'price')
    # Enable searching by title and description for drinks
    search_fields = ('title', 'description')
    # Add filters for status, creation date, and category for drinks
    list_filter = ('status', 'created_on', 'category')
    # Automatically populate the slug field from the title for drinks
    prepopulated_fields = {'slug': ('title',)}
    # Add a date hierarchy for drinks
    date_hierarchy = 'created_on'

    # --- Custom Admin Actions for Drinks ---
    # Defines a custom action to set selected drinks to 'Published' status.
    def change_status_to_published(self, request, queryset):
        queryset.update(status=1) # Update the 'status' field to 1 (Published).
        self.message_user(request, "Selected drinks successfully marked as Published.")
    # The display name in the admin action dropdown.
    change_status_to_published.short_description = "Mark selected drinks as Published" 

    # Defines a custom action to set selected drinks to 'Draft' status.
    def change_status_to_draft(self, request, queryset):
        queryset.update(status=0) # Update the 'status' field to 0 (Draft).
        self.message_user(request, "Selected drinks successfully marked as Draft.")
    # The display name in the admin action dropdown.
    change_status_to_draft.short_description = "Mark selected drinks as Draft" 

    # List of custom actions to be displayed in the admin dropdown.
    actions = ['change_status_to_published', 'change_status_to_draft']