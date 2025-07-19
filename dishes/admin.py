# dishes/admin.py

from django.contrib import admin
# Importiert jetzt sowohl das Dishes- als auch das Drink-Modell
from .models import Category, Dishes, Drink # Importiert unsere Category-, Dishes- und Drink-Modelle.

# Registriert unsere Modelle, damit sie in der Django-Admin-Oberfläche erscheinen.
# Dies macht Category, Dishes und Drink verwaltbar.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Zeigt nur den 'name' in der Admin-Listenansicht für Category-Objekte an.
    list_display = ('name',)
    # Ermöglicht die Suche nach Kategorienamen im Admin.
    search_fields = ('name',)

@admin.register(Dishes) # Registriert das Dishes-Modell
class DishesAdmin(admin.ModelAdmin): # Admin-Klassenname für Dishes
    # Passt an, welche Felder in der Liste der Gerichte im Admin angezeigt werden.
    # 'ingredients' und 'instructions' wurden entfernt, 'price' ist enthalten.
    list_display = ('title', 'category', 'price', 'status', 'created_on', 'author') # HIER: 'ingredients' und 'instructions' entfernt
    # Ermöglicht die Suche nach Titel, Beschreibung und Preis für Gerichte.
    # 'ingredients' und 'instructions' wurden entfernt.
    search_fields = ('title', 'description', 'price') # HIER: 'ingredients' und 'instructions' entfernt
    # Fügt Filter in der Seitenleiste hinzu, um Gerichte nach Status, Erstellungsdatum und Kategorie zu filtern.
    list_filter = ('status', 'created_on', 'category')
    # Sehr praktisch! Wenn ein Titel eingegeben wird, wird das Slug-Feld automatisch ausgefüllt.
    # Das spart Tipparbeit und hilft bei SEO-freundlichen URLs.
    prepopulated_fields = {'slug': ('title',)}
    # Fügt eine Datums-Hierarchie hinzu, um Gerichte nach Jahr, Monat und Tag zu durchsuchen.
    date_hierarchy = 'created_on'

    # --- Benutzerdefinierte Admin-Aktionen für Gerichte ---
    # Definiert eine benutzerdefinierte Aktion, um ausgewählte Gerichte auf den Status 'Published' zu setzen.
    def change_status_to_published(self, request, queryset):
        queryset.update(status=1) # Aktualisiert das Feld 'status' auf 1 (Published).
        self.message_user(request, "Ausgewählte Gerichte erfolgreich als Veröffentlicht markiert.")
    # Der Anzeigename im Admin-Aktions-Dropdown.
    change_status_to_published.short_description = "Ausgewählte Gerichte als Veröffentlicht markieren" 

    # Definiert eine benutzerdefinierte Aktion, um ausgewählte Gerichte auf den Status 'Draft' zu setzen.
    def change_status_to_draft(self, request, queryset):
        queryset.update(status=0) # Aktualisiert das Feld 'status' auf 0 (Draft).
        self.message_user(request, "Ausgewählte Gerichte erfolgreich als Entwurf markiert.")
    # Der Anzeigename im Admin-Aktions-Dropdown.
    change_status_to_draft.short_description = "Ausgewählte Gerichte als Entwurf markieren" 

    # Liste der benutzerdefinierten Aktionen, die im Admin-Dropdown angezeigt werden sollen.
    # Die Standardaktion 'delete_selected' ist automatisch verfügbar.
    actions = ['change_status_to_published', 'change_status_to_draft']


# Registriert das Drink-Modell
@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin): # Admin-Klasse für Drink
    # Passt die Felder an, die in der Admin-Listenansicht für Drink-Objekte angezeigt werden.
    # 'price' ist enthalten.
    list_display = ('title', 'category', 'price', 'status', 'created_on', 'author') # HIER: 'price' hinzugefügt
    # Ermöglicht die Suche nach Titel, Beschreibung und Preis für Getränke.
    search_fields = ('title', 'description', 'price') # HIER: 'price' hinzugefügt
    # Fügt Filter für Status, Erstellungsdatum und Kategorie für Getränke hinzu.
    list_filter = ('status', 'created_on', 'category')
    # Füllt das Slug-Feld automatisch aus dem Titel für Getränke aus.
    prepopulated_fields = {'slug': ('title',)}
    # Fügt eine Datums-Hierarchie hinzu, um Getränke nach Jahr, Monat und Tag zu durchsuchen.
    date_hierarchy = 'created_on'

    # --- Benutzerdefinierte Admin-Aktionen für Getränke ---
    # Definiert eine benutzerdefinierte Aktion, um ausgewählte Getränke auf den Status 'Published' zu setzen.
    def change_status_to_published(self, request, queryset):
        queryset.update(status=1) # Aktualisiert das Feld 'status' auf 1 (Published).
        self.message_user(request, "Ausgewählte Getränke erfolgreich als Veröffentlicht markiert.")
    # Der Anzeigename im Admin-Aktions-Dropdown.
    change_status_to_published.short_description = "Ausgewählte Getränke als Veröffentlicht markieren" 

    # Definiert eine benutzerdefinierte Aktion, um ausgewählte Getränke auf den Status 'Draft' zu setzen.
    def change_status_to_draft(self, request, queryset):
        queryset.update(status=0) # Aktualisiert das Feld 'status' auf 0 (Draft).
        self.message_user(request, "Ausgewählte Getränke erfolgreich als Entwurf markiert.")
    # Der Anzeigename im Admin-Aktions-Dropdown.
    change_status_to_draft.short_description = "Ausgewählte Getränke als Entwurf markieren" 

    # Liste der benutzerdefinierten Aktionen, die im Admin-Dropdown angezeigt werden sollen.
    # Die Standardaktion 'delete_selected' ist automatisch verfügbar.
    actions = ['change_status_to_published', 'change_status_to_draft']