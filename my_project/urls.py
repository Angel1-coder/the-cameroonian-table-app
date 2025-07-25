# my_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Import settings
from django.conf.urls.static import static # Import static
from dishes import views as dishes_views

urlpatterns = [
    path('', dishes_views.index, name='home'),
    path('admin/', admin.site.urls),
]

# This block is used to serve media files (like images) during development.
# In a production environment, this is handled differently.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)