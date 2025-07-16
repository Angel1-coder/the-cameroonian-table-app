# my_project/urls.py

from django.contrib import admin
from django.urls import path, include
from dishes import views as dishes_views 

urlpatterns = [
    path('', dishes_views.index, name='home'), 
    path('admin/', admin.site.urls),
]