# dishes/models.py

from django.db import models
from django.contrib.auth.models import User # Imports Django's built-in User model for dish authorship.

# Defines categories for menu items (e.g., Appetizers, Main Courses, Desserts, Drinks, etc.).
# Using a separate model for categories promotes data normalization and easier management.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # Unique name for the category.

    class Meta:
        verbose_name_plural = "Categories" # Correct pluralization for the admin interface.
        ordering = ['name'] # Orders categories alphabetically by name.

    def __str__(self):
        return self.name # Returns the category name for display.

# Represents a single dish on the restaurant's menu.
class Dishes(models.Model): # The model name is Dishes, as requested
    title = models.CharField(max_length=200, unique=True) # Unique title for the dish.
    slug = models.SlugField(max_length=200, unique=True) # URL-friendly identifier, unique for each dish.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dish_posts"
    ) # Links to the User who added the dish; dishes are deleted if the author is.
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="dishes_in_category"
    ) # Links to a Category; the category link is set to NULL if the category is deleted. Optional field.

    description = models.TextField(blank=True) # Optional short description of the dish.
    # ingredients field removed as requested
    # instructions field removed as requested
    
    # Defines the publication status of the dish (Draft or Published).
    STATUS = ((0, "Draft"), (1, "Published"))
    status = models.IntegerField(choices=STATUS, default=0)

    created_on = models.DateTimeField(auto_now_add=True) # Automatically set on creation.
    updated_on = models.DateTimeField(auto_now=True) # Automatically updated on each save.

    # image = models.ImageField(upload_to='dish_images/', blank=True, null=True) # Placeholder for image integration (e.g., Cloudinary).

    class Meta:
        ordering = ["-created_on"] # Orders dishes by creation date, newest first.
        verbose_name_plural = "Dishes" # Correct pluralization for the admin interface.

    def __str__(self):
        return self.title # Returns the dish title for object representation.

# NEW MODEL: Represents a single drink on the restaurant's menu.
class Drink(models.Model):
    title = models.CharField(max_length=200, unique=True) # Unique title for the drink.
    slug = models.SlugField(max_length=200, unique=True) # URL-friendly identifier, unique for each drink.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="drink_posts"
    ) # Links to the User who added the drink; drinks are deleted if the author is.
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="drinks_in_category"
    ) # Links to a Category; the category link is set to NULL if the category is deleted. Optional field.

    description = models.TextField(blank=True) # Optional short description of the drink.
    # We don't need ingredients/instructions for drinks on the public menu
    
    # Defines the publication status of the drink (Draft or Published).
    STATUS = ((0, "Draft"), (1, "Published"))
    status = models.IntegerField(choices=STATUS, default=0)

    created_on = models.DateTimeField(auto_now_add=True) # Automatically set on creation.
    updated_on = models.DateTimeField(auto_now=True) # Automatically updated on each save.

    class Meta:
        ordering = ["title"] # Orders drinks alphabetically by title.
        verbose_name_plural = "Drinks" # Correct pluralization for the admin interface.

    def __str__(self):
        return self.title # Returns the drink title for object representation.