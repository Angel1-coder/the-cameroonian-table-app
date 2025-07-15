# dishes/admin.py

from django.contrib import admin
from .models import Category, Dish # Importiere unsere neuen Modelle Category und Dish

# Hier registrieren wir unsere Modelle.
# Das macht die Category- und Dish-Modelle im Django-Admin-Interface sichtbar und verwaltbar.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Optional: Anpassen, wie Category-Objekte in der Admin-Liste angezeigt werden.
    # Wir wollen einfach nur den Namen sehen.
    list_display = ('name',)
    # Ermöglicht die Suche nach Kategorienamen.
    search_fields = ('name',)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    # Anpassen, welche Felder in der Liste der Gerichte im Admin angezeigt werden.
    # So haben wir schnell einen Überblick über Titel, Kategorie, Status, Erstellungsdatum und Verfasser.
    list_display = ('title', 'category', 'status', 'created_on', 'author')
    # Ermöglicht die Suche nach Titel und Beschreibung des Gerichts.
    search_fields = ('title', 'description')
    # Fügt Filter in der Seitenleiste hinzu, um Gerichte nach Status, Erstellungsdatum und Kategorie zu filtern.
    list_filter = ('status', 'created_on', 'category')
    # Das ist super praktisch! Wenn wir einen Titel eingeben, wird der Slug automatisch ausgefüllt.
    # Das spart Tipparbeit und hilft bei SEO-freundlichen URLs.
    prepopulated_fields = {'slug': ('title',)}
    # Fügt eine Datums-Hierarchie hinzu, um Gerichte nach Jahr, Monat, Tag zu durchsuchen.
    date_hierarchy = 'created_on'
    