# recipes/models.py

from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model for dish authorship.

# Defines categories for menu items (e.g., Appetizers, Main Courses, Desserts).
# Using a separate model for categories promotes data normalization and easier management.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # Unique name for the category.

    class Meta:
        verbose_name_plural = "Categories" # Correct pluralization for the admin interface.
        ordering = ['name'] # Orders categories alphabetically by name.

    def __str__(self):
        return self.name # Returns the category name for display.

# Represents a single dish on the restaurant's menu.
class Dish(models.Model):
    title = models.CharField(max_length=200, unique=True) # Unique title for the dish.
    slug = models.SlugField(max_length=200, unique=True) # URL-friendly identifier, unique for each dish.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dish_posts"
    ) # Links to the User who added the dish; dishes are deleted if the author is.
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="dishes_in_category"
    ) # Links to a Category; category link is set to NULL if the category is deleted. Optional field.

    description = models.TextField(blank=True) # Optional short description of the dish.
    ingredients = models.TextField() # Detailed list of ingredients.
    instructions = models.TextField() # Preparation instructions for the dish.
    
    # Defines the publication status of the dish (Draft or Published).
    STATUS = ((0, "Draft"), (1, "Published"))
    status = models.IntegerField(choices=STATUS, default=0)

    created_on = models.DateTimeField(auto_now_add=True) # Automatically set on creation.
    updated_on = models.DateTimeField(auto_now=True) # Automatically updated on each save.

    # image = models.ImageField(upload_to='dish_images/', blank=True, null=True) # Placeholder for image integration (e.g., Cloudinary).

    class Meta:
        ordering = ["-created_on"] # Orders dishes by creation date, newest first.

    def __str__(self):
        return self.title # Returns the dish title for object representation.
    