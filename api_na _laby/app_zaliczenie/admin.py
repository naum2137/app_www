from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User, Book, Category, Rental, BookReservation

# Niestandardowy formularz edycji użytkownika
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'is_superuser')

# Niestandardowy UserAdmin
class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')  # Filtry w panelu
    search_fields = ('username', 'email')  # Pole wyszukiwania

# Rejestracja użytkownika w panelu administratora
admin.site.register(User, CustomUserAdmin)

# Rejestracja modelu książek
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'available')  # Pola do wyświetlania
    list_filter = ('available', 'category')  # Filtry w panelu
    search_fields = ('title', 'author')  # Pole wyszukiwania

# Rejestracja modelu kategorii
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Wyświetlanie ID i nazwy kategorii
    search_fields = ('name',)  # Pole wyszukiwania po nazwie

# Rejestracja modelu wypożyczeń
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'rental_date', 'return_date', 'status')
    list_filter = ('status',)  # Filtr na status wypożyczenia
    search_fields = ('user__username', 'book__title')  # Wyszukiwanie po użytkowniku i książce

# Rejestracja modelu rezerwacji książek
@admin.register(BookReservation)
class BookReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'reservation_date', 'expiration_date', 'status')
    list_filter = ('status',)  # Filtr na status rezerwacji
    search_fields = ('user__username', 'book__title')  # Wyszukiwanie po użytkowniku i książce
