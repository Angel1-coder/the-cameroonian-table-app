# dishes/models.py

from django.db import models
from django.contrib.auth.models import User # Imports Django's built-in User model for dish authorship.

# Defines categories for menu items (e.g., Starters, Mains, Desserts, Drinks, etc.).
# Using a separate model for categories promotes data normalization and easier management.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # Unique name for the category.

    class Meta:
        verbose_name_plural = "Categories" # Correct plural form for the admin interface.
        ordering = ['name'] # Orders the categories alphabetically by name.

    def __str__(self):
        return self.name # Returns the category name for display.

# Represents a single dish on the restaurant menu.
class Dishes(models.Model): # The model name is Dishes as requested.
    title = models.CharField(max_length=200, unique=True) # Unique title for the dish.
    slug = models.SlugField(max_length=200, unique=True) # A URL-friendly identifier, unique to each dish.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dish_posts"
    ) # Links to the User who added the dish; dishes are deleted if the author is deleted.
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="dishes_in_category"
    ) # Links to a category; the category link is set to NULL if the category is deleted. This field is optional.

    description = models.TextField(blank=True) # Optional brief description of the dish.
    # ingredients = models.TextField(blank=True) # Detailed list of ingredients. REMOVED AS REQUESTED.
    # instructions = models.TextField(blank=True) # Preparation instructions for the dish. REMOVED AS REQUESTED.
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00) # NEW: Price field for dishes.
    
    # Defines the publication status of the dish (Draft or Published).
    STATUS = ((0, "Draft"), (1, "Published"))
    status = models.IntegerField(choices=STATUS, default=0)

    created_on = models.DateTimeField(auto_now_add=True) # Automatically set on creation.
    updated_on = models.DateTimeField(auto_now=True) # Automatically updated on every save.

    # image = models.ImageField(upload_to='dish_images/', blank=True, null=True) # Placeholder for image integration (e.g., Cloudinary).

    class Meta:
        ordering = ["-created_on"] # Orders the dishes by creation date, newest first.
        verbose_name_plural = "Dishes" # Correct plural form for the admin interface.

    def __str__(self):
        return self.title # Returns the dish title for object representation.

# NEW MODEL: Represents a single drink on the restaurant menu.
class Drink(models.Model):
    title = models.CharField(max_length=200, unique=True) # Unique title for the drink.
    slug = models.SlugField(max_length=200, unique=True) # A URL-friendly identifier, unique to each drink.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="drink_posts"
    ) # Links to the User who added the drink; drinks are deleted if the author is deleted.
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="drinks_in_category"
    ) # Links to a category; the category link is set to NULL if the category is deleted. This field is optional.

    description = models.TextField(blank=True) # Optional brief description of the drink.
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00) # NEW: Price field for drinks.
    # Ingredients/instructions are not required for drinks on the public menu.
    
    # Defines the publication status of the drink (Draft or Published).
    STATUS = ((0, "Draft"), (1, "Published"))
    status = models.IntegerField(choices=STATUS, default=0)

    created_on = models.DateTimeField(auto_now_add=True) # Automatically set on creation.
    updated_on = models.DateTimeField(auto_now=True) # Automatically updated on every save.

    class Meta:
        ordering = ["title"] # Orders the drinks alphabetically by title.
        verbose_name_plural = "Drinks" # Correct plural form for the admin interface.

    def __str__(self):
        return self.title # Returns the drink title for object representation.

# NEW MODEL: Represents table reservations made by customers
class Reservation(models.Model):
    name = models.CharField(max_length=100) # Customer's full name
    email = models.EmailField() # Customer's email for confirmation
    phone = models.CharField(max_length=20, blank=True) # Optional phone number
    guests = models.PositiveIntegerField() # Number of guests (minimum 1)
    date = models.DateField() # Reservation date
    time = models.TimeField() # Reservation time
    created_on = models.DateTimeField(auto_now_add=True) # When reservation was made
    updated_on = models.DateTimeField(auto_now=True) # Last update timestamp
    
    # Reservation status choices
    STATUS = ((0, "Pending"), (1, "Confirmed"), (2, "Cancelled"))
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ["-created_on"] # Newest reservations first
        verbose_name_plural = "Reservations"
    
    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"