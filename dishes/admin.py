from django.contrib import admin
from .models import Category, Dishes, Drink, Reservation 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'status', 'created_on', 'author')
    search_fields = ('title', 'description')
    list_filter = ('status', 'created_on', 'category')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_on'

    def change_status_to_published(self, request, queryset):
        queryset.update(status=1)
        self.message_user(request, "Selected dishes successfully marked as Published.")
    change_status_to_published.short_description = "Mark selected dishes as Published" 

    def change_status_to_draft(self, request, queryset):
        queryset.update(status=0)
        self.message_user(request, "Selected dishes successfully marked as Draft.")
    change_status_to_draft.short_description = "Mark selected dishes as Draft" 

    actions = ['change_status_to_published', 'change_status_to_draft']


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'status', 'created_on', 'author')
    search_fields = ('title', 'description')
    list_filter = ('status', 'created_on', 'category')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_on'

    def change_status_to_published(self, request, queryset):
        queryset.update(status=1)
        self.message_user(request, "Selected drinks successfully marked as Published.")
    change_status_to_published.short_description = "Mark selected drinks as Published" 

    def change_status_to_draft(self, request, queryset):
        queryset.update(status=0)
        self.message_user(request, "Selected drinks successfully marked as Draft.")
    change_status_to_draft.short_description = "Mark selected drinks as Draft" 

    actions = ['change_status_to_published', 'change_status_to_draft']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'guests', 'date', 'time', 'status', 'created_on')
    search_fields = ('name', 'email')
    list_filter = ('status', 'date', 'created_on')
    date_hierarchy = 'created_on'
    readonly_fields = ('created_on', 'updated_on')

    def mark_as_confirmed(self, request, queryset):
        queryset.update(status=1)
        self.message_user(request, "Selected reservations marked as confirmed.")
    mark_as_confirmed.short_description = "Mark as confirmed"

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status=2)
        self.message_user(request, "Selected reservations marked as cancelled.")
    mark_as_cancelled.short_description = "Mark as cancelled"

    actions = ['mark_as_confirmed', 'mark_as_cancelled']
