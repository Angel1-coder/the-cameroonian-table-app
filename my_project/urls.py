# my_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # <-- ADD THIS LINE: Imports Django's settings.
from django.conf.urls.static import static # <-- ADD THIS LINE: Imports static URL patterns helper.
from dishes import views as dishes_views

urlpatterns = [
    path('', dishes_views.index, name='home'),
    path('admin/', admin.site.urls),
]

# This block is for serving media files during development.
# In a production environment, a dedicated web server (like Nginx or Apache)
# would be configured to serve these files directly.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)