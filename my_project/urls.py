# my_project/urls.py

from django.contrib import admin
from django.urls import path, include
from dishes import views as dishes_views

urlpatterns = [
    # This path routes the root URL ('') to the 'index' view in my 'dishes' app.
    # I've named it 'home' for easy reference in my templates.
    path('', dishes_views.index, name='home'), 
    # This path provides access to Django's built-in administration site.
    path('admin/', admin.site.urls), 
]